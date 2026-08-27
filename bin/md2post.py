#!/usr/bin/env python3
"""Compile a markdown article into a styled blog post (writing/<slug>/index.html).

The article stays in .md; this tool applies the house template
(_templates/blog-post/index.html — header, byline strip, scroll-spy TOC,
section styling, BibTeX citation) at build time.

Usage:
    python3 bin/md2post.py path/to/article.md [--out writing/<slug>] [--site]

Front matter (YAML, required keys marked *):
    title*:        Post title
    slug*:         URL slug (writing/<slug>/)
    description*:  One-line description for og/twitter cards
    date:          "July 21, 2026"  (defaults to today)
    affiliation:   defaults "Independent"
    author:        defaults "Lily Zhang"
    bibkey:        defaults zhang<year><slug-word>

Body conventions:
    ## Heading        -> numbered section (1 · Heading) + TOC entry
    ### Subheading    -> numbered subsection (1.1 ·) + indented TOC entry
    ## References / ## Appendix  -> unnumbered
    Citation section is generated automatically from front matter.
    Images: ![alt](fig.png "Figure 1. Caption") -> <figure> with caption.
"""
import argparse, datetime, html, pathlib, re, shutil, sys

import markdown
import yaml

REPO = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "_templates/blog-post/index.html"
UNNUMBERED = {"references", "appendix", "acknowledgements", "citation"}


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def parse_front_matter(src):
    m = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", src, re.S)
    if not m:
        sys.exit("error: markdown file needs YAML front matter (--- ... ---)")
    return yaml.safe_load(m.group(1)), m.group(2)


def protect_math(md):
    """Stash math spans before markdown conversion so the LaTeX survives intact.

    Posts write math wrapped in double backslashes: \\x\\ inline, and a whole
    paragraph as \\ X \\ for display math. Raw markdown conversion mangles the
    LaTeX (eats backslash escapes, may italicize underscores), so we swap each
    span for a placeholder here and restore_math() puts it back as MathJax
    delimiters (\\(...\\) inline, \\[...\\] display) after rendering.
    """
    stash = []

    def unescape(tex):
        # mirror markdown's backslash-escape processing (\_ -> _, \* -> *, ...),
        # but keep \\ which is a LaTeX line break, not an escape
        tex = tex.replace("\\\\", "\x00")
        tex = re.sub(r"\\([\\`*_{}\[\]()#+\-.!])", r"\1", tex)
        return tex.replace("\x00", "\\\\")

    def take(m, display):
        stash.append((unescape(m.group(1)), display))
        return f"MATHSTASH{len(stash) - 1}Z"

    # display: a line fully wrapped in \\ ... \\  (may contain \\ line breaks)
    md = re.sub(r"(?m)^\\\\ (.+) \\\\$", lambda m: take(m, True), md)
    # inline: \\...\\
    md = re.sub(r"\\\\(.+?)\\\\", lambda m: take(m, False), md)
    return md, stash


def restore_math(html_text, stash):
    for i, (tex, display) in enumerate(stash):
        if display:
            html_text = html_text.replace(f"<p>MATHSTASH{i}Z</p>", f"<p>\\[{tex}\\]</p>")
        html_text = html_text.replace(f"MATHSTASH{i}Z", f"\\({tex}\\)")
    return html_text


def build_sections(md_body):
    """Render markdown, then wrap each h2 block in <section id>, numbering h2/h3."""
    md_body, math_stash = protect_math(md_body)
    rendered = markdown.markdown(
        md_body,
        extensions=["tables", "fenced_code", "footnotes", "attr_list", "md_in_html"],
    )
    rendered = restore_math(rendered, math_stash)
    # split on h2
    parts = re.split(r"(<h2[^>]*>.*?</h2>)", rendered)
    pre = parts[0].strip()
    # lede = first <p> before any heading; anything after it (teaser figures
    # etc.) is kept as a raw preamble block
    m = re.match(r"<p>(.*?)</p>\s*(.*)", pre, re.S)
    lede_html = f"<p>{m.group(1)}</p>" if m else pre
    preamble = m.group(2).strip() if m else ""
    sections, toc = [], []
    num = 0
    for i in range(1, len(parts), 2):
        heading = re.sub(r"</?h2[^>]*>", "", parts[i]).strip()
        id_m = re.search(r'id="([^"]+)"', parts[i])
        body = parts[i + 1] if i + 1 < len(parts) else ""
        sec_id = id_m.group(1) if id_m else slugify(heading)
        if slugify(heading) in UNNUMBERED:
            h2 = f"<h2>{heading}</h2>"
            toc.append((sec_id, heading, False))

            def plain_h3(m3):
                text = m3.group(2).strip()
                id3 = re.search(r'id="([^"]+)"', m3.group(1))
                h3_id = id3.group(1) if id3 else slugify(text)
                toc.append((h3_id, text, True))
                return f'<h3 id="{h3_id}">{text}</h3>'
            body = re.sub(r"<h3([^>]*)>(.*?)</h3>", plain_h3, body)
        else:
            num += 1
            h2 = f"<h2>{num} · {heading}</h2>"
            toc.append((sec_id, f"{num} · {heading}", False))
            # number h3s within this section
            sub = 0
            def number_h3(m3, num=num):
                nonlocal sub
                sub += 1
                text = m3.group(2).strip()
                id3 = re.search(r'id="([^"]+)"', m3.group(1))
                h3_id = id3.group(1) if id3 else slugify(text)
                toc.append((h3_id, f"{num}.{sub} · {text}", True))
                return f'<h3 id="{h3_id}">{num}.{sub} · {text}</h3>'
            body = re.sub(r"<h3([^>]*)>(.*?)</h3>", number_h3, body)
        sections.append(f'    <section id="{sec_id}">\n      {h2}\n{body}\n    </section>')
    return lede_html, preamble, sections, toc


def figureize(html_text):
    """<p><img alt title></p> -> <figure><img><figcaption></figure>."""
    def repl(m):
        img = m.group(1)
        t = re.search(r'title="([^"]*)"', img)
        cap = ""
        if t:
            caption = t.group(1)
            caption = re.sub(r"^(Figure \d+\.)", r"<strong>\1</strong>", caption)
            cap = f"\n        <figcaption>{caption}</figcaption>"
            img = img.replace(f' title="{t.group(1)}"', "")
        return f'      <figure class="mid">\n        {img}{cap}\n      </figure>'
    return re.sub(r"<p>(<img [^>]*>)</p>", repl, html_text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mdfile")
    ap.add_argument("--out", help="output dir (default writing/<slug>)")
    ap.add_argument("--site", action="store_true", help="also copy into _site/ for the local server")
    args = ap.parse_args()

    meta, body = parse_front_matter(pathlib.Path(args.mdfile).read_text())
    for k in ("title", "slug", "description"):
        if k not in meta:
            sys.exit(f"error: front matter missing '{k}'")

    today = datetime.date.today()
    date = str(meta.get("date") or today.strftime("%B %-d, %Y"))
    year = re.search(r"\d{4}", date).group(0)
    month = date.split()[0]
    author = meta.get("author", "Lily Zhang")
    affiliation = meta.get("affiliation", "Independent")
    bibkey = meta.get("bibkey", f"zhang{year}{meta['slug'].split('-')[0]}")

    lede, preamble, sections, toc = build_sections(body)
    sections = [figureize(s) for s in sections]

    # citation section from front matter
    bib = (f"@article{{{bibkey},\n"
           f'  title   = "{meta["title"]}",\n'
           f'  author  = "Zhang, Lily",\n'
           f'  year    = "{year}",\n'
           f'  month   = "{month}",\n'
           f'  url     = "https://lilyzh.ng/writing/{meta["slug"]}/"\n}}')
    sections.append(
        '    <section id="citation">\n      <h2>Citation</h2>\n'
        "      <p>You can cite this post here:</p>\n"
        '      <div class="bibtex-block">\n'
        '        <button class="bibtex-copy" type="button">Copy</button>\n'
        f"        <pre><code>{html.escape(bib)}</code></pre>\n"
        "      </div>\n    </section>"
    )
    toc.append(("citation", "Citation", False))

    toc_html = "\n".join(
        f'      <li{" class=" + chr(34) + "sub" + chr(34) if sub else ""}><a href="#{i}">{t}</a></li>'
        for i, t, sub in toc
    )

    tpl = TEMPLATE.read_text()
    head = tpl[: tpl.index('  <aside class="toc"')]
    tail = tpl[tpl.index("</div>\n\n<script>") :]

    head = (head.replace("POST_TITLE", html.escape(meta["title"]))
                .replace("POST_SLUG", meta["slug"])
                .replace("POST_DESCRIPTION", html.escape(meta["description"])))

    # per-post extra styles: custom.css next to the md file
    custom_css = pathlib.Path(args.mdfile).resolve().parent / "custom.css"
    if custom_css.exists():
        head = head.replace("</head>", f"<style>\n{custom_css.read_text()}\n</style>\n</head>")

    lede_block = f'\n    <p class="lede">{re.sub(r"^<p>|</p>$", "", lede)}</p>\n' if lede else ""
    page = (
        head
        + '  <aside class="toc" aria-label="Table of contents">\n'
        + '    <div class="toc-title">Table of Contents</div>\n    <ul>\n'
        + toc_html + "\n    </ul>\n  </aside>\n\n  <article>\n"
        + f"    <h1>{html.escape(meta['title'])}</h1>\n"
        + '    <div class="authors">\n'
        + '      <span class="byline-col">\n        <span class="byline-label">Authors</span>\n'
        + f'        <span class="byline-value">{author}</span>\n      </span>\n'
        + '      <span class="byline-col">\n        <span class="byline-label">Affiliations</span>\n'
        + f'        <span class="byline-value light">{affiliation}</span>\n      </span>\n'
        + '      <span class="byline-col">\n        <span class="byline-label">Published</span>\n'
        + f'        <span class="byline-value light">{date}</span>\n      </span>\n    </div>\n'
        + lede_block + (("\n" + preamble + "\n") if preamble else "") + "\n"
        + "\n\n".join(sections)
        + "\n  </article>\n"
        + tail
    )

    out = pathlib.Path(args.out) if args.out else REPO / "writing" / meta["slug"]
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page)
    print(f"wrote {out / 'index.html'}")

    # copy post assets (images) sitting next to the md file
    src_dir = pathlib.Path(args.mdfile).resolve().parent
    for img in list(src_dir.glob("*.png")) + list(src_dir.glob("*.jpg")) + list(src_dir.glob("*.svg")):
        if src_dir != out.resolve():
            shutil.copy(img, out / img.name)
            print(f"copied {img.name}")

    if args.site:
        site_out = REPO / "_site" / "writing" / meta["slug"]
        site_out.mkdir(parents=True, exist_ok=True)
        for f in out.iterdir():
            if f.is_dir():
                shutil.copytree(f, site_out / f.name, dirs_exist_ok=True)
            else:
                shutil.copy(f, site_out / f.name)
        print(f"copied to {site_out}")


if __name__ == "__main__":
    main()
