# Blog post template

Derived from `writing/c-guard/index.html` (2026-08-25). To start a new post:

1. Create `writing/<slug>/article.md` (see the front matter spec in `bin/md2post.py`), images beside it.
2. Replace the placeholders: `POST_TITLE`, `POST_SLUG`, `POST_DESCRIPTION`, `MONTH DAY, YEAR`, `YEAR`, `zhangYEARslug`.
3. Update the TOC `<li>` list to match your `<section id=...>` headings (use `class="sub"` for subsections).
4. Add an `og-image.png` in the post folder for social cards.

Notes:
- The site header (name + Home/Writing/Projects/Talks) is shared CSS: `/assets/css/blog-header.css`. Do NOT copy header styles inline; edit that one file to change all posts.
- The `_templates/` folder starts with `_` so Jekyll does not publish it.
- Scroll-spy TOC highlighting and the BibTeX copy button are wired in the inline script at the bottom; they work off the section ids automatically.
