#!/usr/bin/env python3
"""One-time reverse-converter: extract posts/<slug>/article.md (+ custom.css,
images) from a hand-written writing/<slug>/index.html, so the post can be
maintained as markdown and compiled by bin/md2post.py.

Simple paragraphs and headings become markdown (via pandoc); figures, tables,
code blocks, and bespoke divs are kept as raw HTML blocks (markdown passes
block-level HTML through untouched). Post-specific CSS (rules not present in
the shared template) is saved to custom.css, which md2post.py injects.

Usage: python3 bin/html2md.py <slug> [<slug> ...]
"""
import pathlib, re, shutil, subprocess, sys

import lxml.html

REPO = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "_templates/blog-post/index.html"


def pandoc_md(html_snippet):
    return subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm-raw_html+tex_math_dollars", "--wrap=none"],
        input=html_snippet, capture_output=True, text=True, check=True,
    ).stdout.strip()


def inner_html(el):
    s = (el.text or "") + "".join(
        lxml.html.tostring(c, encoding="unicode") for c in el
    )
    return s.strip()


def outer_html(el):
    return lxml.html.tostring(el, encoding="unicode").strip()


def strip_number(text):
    # strips "1 · ", "1. ", "2.1 · ", "2.1. ", leading "01" from sec-num remnants
    return re.sub(r"^\s*\d+(\.\d+)*\s*[·.]?\s+", "", text).strip()


SIMPLE_INLINE = {"a", "strong", "em", "code", "b", "i", "span", "br", "sup", "sub"}


def block_to_md(el):
    tag = el.tag
    if tag == "p" and all(c.tag in SIMPLE_INLINE for c in el) and el.get("class") is None:
        return pandoc_md(outer_html(el))
    if tag in ("ul", "ol") and not el.xpath('.//figure|.//table|.//pre|.//div'):
        return pandoc_md(outer_html(el))
    if tag == "h3":
        txt = strip_number(el.text_content())
        hid = el.get("id")
        return f"### {txt} {{#{hid}}}" if hid else f"### {txt}"
    if tag == "h4":
        return f"#### {el.text_content().strip()}"
    return outer_html(el)  # figures, tables, pre, blockquotes, custom divs: raw HTML


def css_blocks(css_text):
    """Split stylesheet text into top-level blocks (rule or @media), normalized."""
    blocks, depth, start = [], 0, 0
    for i, ch in enumerate(css_text):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                blocks.append(css_text[start : i + 1])
                start = i + 1
    return blocks


def norm(block):
    return re.sub(r"\s+", " ", block).strip()


def convert(slug):
    src = REPO / "writing" / slug / "index.html"
    doc = lxml.html.fromstring(src.read_text())

    def meta_content(sel):
        el = doc.xpath(sel)
        return el[0].get("content") if el else ""

    title = meta_content('//meta[@property="og:title"]') or doc.xpath("//title")[0].text
    desc = meta_content('//meta[@property="og:description"]')
    byline_vals = [e.text_content().strip() for e in doc.xpath('//div[@class="authors"]//span[contains(@class,"byline-value")]')]
    date = byline_vals[2] if len(byline_vals) >= 3 else ""
    affiliation = byline_vals[1] if len(byline_vals) >= 2 else "Independent"
    bib = doc.xpath('//div[@class="bibtex-block"]//code')
    bibkey = ""
    if bib:
        m = re.search(r"@\w+\{([^,]+),", bib[0].text_content())
        bibkey = m.group(1) if m else ""

    lede_el = doc.xpath('//p[@class="lede"]')
    lede = pandoc_md(inner_html(lede_el[0])) if lede_el else ""

    out_lines = []

    def emit_section(sec):
        sid = sec.get("id", "")
        if sid == "citation":
            return
        kids = [c for c in sec if isinstance(c.tag, str)]
        if not kids:
            return
        head_el = kids[0] if kids[0].tag in ("h2", "h3") else None
        if head_el is not None:
            for sn in head_el.xpath('.//*[contains(@class,"sec-num")]'):
                sn.drop_tree()
            heading = strip_number(head_el.text_content())
            level = "##" if head_el.tag == "h2" else "###"
            out_lines.append(f"{level} {heading} {{#{sid}}}\n" if sid else f"{level} {heading}\n")
        for child in kids:
            if child is head_el:
                continue
            if child.tag == "section":
                emit_section(child)
            else:
                out_lines.append(block_to_md(child) + "\n")

    article = doc.xpath("//article")[0]
    for child in article:
        if not isinstance(child.tag, str):
            continue
        if child.tag == "h1" or (child.get("class") or "") in ("authors", "lede"):
            continue
        if child.tag == "p" and "lede" in (child.get("class") or ""):
            continue
        if child.tag == "section":
            emit_section(child)
        else:
            out_lines.append(block_to_md(child) + "\n")

    fm = ['---', f'title: "{title}"', f"slug: {slug}", f'description: "{desc}"']
    if date:
        fm.append(f'date: "{date}"')
    if affiliation:
        fm.append(f"affiliation: {affiliation}")
    if bibkey:
        fm.append(f"bibkey: {bibkey}")
    fm.append("---\n")

    out_dir = REPO / "posts" / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "article.md").write_text(
        "\n".join(fm) + "\n" + lede + "\n\n" + "\n".join(out_lines)
    )

    # post-specific CSS = style blocks not present in the template
    tpl_doc = lxml.html.fromstring(TEMPLATE.read_text())
    tpl_norms = {
        norm(b) for st in tpl_doc.xpath("//style") for b in css_blocks(st.text or "")
    }
    extra = [
        b.strip()
        for st in doc.xpath("//style")
        for b in css_blocks(st.text or "")
        if norm(b) not in tpl_norms
    ]
    if extra:
        (out_dir / "custom.css").write_text("\n".join(extra) + "\n")

    # copy post assets so posts/<slug>/ is the self-contained source
    for f in (REPO / "writing" / slug).iterdir():
        if f.is_dir():
            shutil.copytree(f, out_dir / f.name, dirs_exist_ok=True)
        elif f.suffix.lower() in (".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp", ".mp4", ".woff"):
            shutil.copy(f, out_dir / f.name)

    print(f"{slug}: article.md ({len(out_lines)} blocks), custom.css ({len(extra)} rules)")


if __name__ == "__main__":
    for slug in sys.argv[1:]:
        convert(slug)
