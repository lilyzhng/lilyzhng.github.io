---
layout: splash
title: "Lily Zhang | Posts"
permalink: /posts/
---

<div class="header-container">
  <div class="name-container">
    <h1 class="author-name">Lily Zhang</h1>
  </div>
  <div class="navigation-container">
    <a href="/" class="nav-link">Home</a>
    <a href="/posts" class="nav-link">Posts</a>
    <a href="/papers" class="nav-link">Papers</a>
  </div>
</div>

<div class="posts-layout">
  <nav class="posts-filter" aria-label="Post type filter">
    <button class="filter-item is-active" data-filter="blog">Blog</button>
    <button class="filter-item" data-filter="thoughts">Thoughts</button>
    <button class="filter-item" data-filter="all">All</button>
  </nav>

  <div class="blog-list">
  <div class="blog-entry" data-type="blog">
    <a href="/posts/c-guard/" class="blog-title">A Constitution-Grid Instrument for Data-Efficient RL Alignment (C-Guard)</a>
    <span class="blog-date">07.21.26</span>
  </div>

  <div class="blog-entry" data-type="thoughts">
    <a href="https://x.com/lily_gpupoor/status/2076794330401087964" class="blog-title" target="_blank">My Take on the $100B Market for AI Training Data, Including RL Environments</a>
    <span class="blog-date">07.13.26</span>
  </div>

  <div class="blog-entry" data-type="thoughts">
    <a href="https://x.com/lily_gpupoor/status/2076114858203095503" class="blog-title" target="_blank">Second-Order Effects After Cursor and Cognition Cracked Post-Training</a>
    <span class="blog-date">07.12.26</span>
  </div>

  <div class="blog-entry" data-type="thoughts">
    <a href="https://x.com/lily_gpupoor/status/2074728312161849627" class="blog-title" target="_blank">Reflection: Where Is the Market for Post-Training as a Service?</a>
    <span class="blog-date">07.08.26</span>
  </div>

  <div class="blog-entry" data-type="thoughts">
    <a href="https://x.com/lily_gpupoor/status/2072083403898507278" class="blog-title" target="_blank">AI Engineer World's Fair: Is Speculative Decoding All We Need?</a>
    <span class="blog-date">06.30.26</span>
  </div>

  <div class="blog-entry" data-type="blog">
    <a href="https://x.com/lily_gpupoor/status/2070401977251659794" class="blog-title" target="_blank">Build a Dense Reward for Your Writing</a>
    <span class="blog-date">06.26.26</span>
  </div>

  <div class="blog-entry" data-type="blog">
    <a href="/posts/harbor-rlvr-environment/" class="blog-title">What Can't Be Measured Can't Be Solved: RLVR Environment Design from a Failure Taxonomy</a>
    <span class="blog-date">06.10.26</span>
  </div>

  <div class="blog-entry" data-type="blog">
    <a href="/posts/interaction-model/" class="blog-title">Thoughts on Thinking Machine's Interaction Model</a>
    <span class="blog-date">05.20.26</span>
  </div>

  <div class="blog-entry" data-type="blog">
    <a href="https://skill-claw.vercel.app/" class="blog-title" target="_blank">Skill Claw: Self-Improving Robot Agents</a>
    <span class="blog-date">03.15.26</span>
  </div>

  <div class="blog-entry" data-type="blog">
    <a href="https://supergeneral.vercel.app/" class="blog-title" target="_blank">SuperGeneral: Compositional Tool Environments for Agent Training</a>
    <span class="blog-date">03.10.26</span>
  </div>

  <div class="blog-entry" data-type="thoughts">
    <a href="https://github.com/zarazhangrui/frontend-slides" class="blog-title" target="_blank">Frontend Slides: AI-Native Presentation Generation</a>
    <span class="blog-date">02.27.26</span>
  </div>

  <div class="blog-entry" data-type="blog">
    <a href="https://sofagenius.ai/" class="blog-title" target="_blank">SofaGenius: Multi-Agent ML Research Assistant</a>
    <span class="blog-date">02.21.26</span>
  </div>

  <div class="blog-entry" data-type="thoughts">
    <a href="/posts/ieee-most-panel" class="blog-title">IEEE MOST Panel: Driving Force Towards Large-Scale AV Commercialization</a>
    <span class="blog-date">05.05.25</span>
  </div>

  </div>
</div>

<div class="motto-section">
  <div class="motto-container">
    <div class="motto-quote">
      Pain is inevitable but suffering is optional
    </div>
    <div class="motto-attribution">
      — Haruki Murakami
    </div>

  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function () {
  var buttons = document.querySelectorAll('.posts-filter .filter-item');
  var entries = document.querySelectorAll('.blog-entry');
  function apply(f) {
    entries.forEach(function (e) {
      e.style.display = (f === 'all' || e.getAttribute('data-type') === f) ? '' : 'none';
    });
  }
  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      buttons.forEach(function (b) { b.classList.remove('is-active'); });
      btn.classList.add('is-active');
      apply(btn.getAttribute('data-filter'));
    });
  });
  apply('blog');   // Blog is the default view
});
</script>

<style>
/* Header + nav come from the shared site CSS (main.css) via the splash layout,
   so this page matches Home and Papers exactly (background, zoom, header). */

/* Pin the footer to the viewport bottom when the (filtered) list is short:
   stretch the page's wrapper chain and let the motto take the slack. */
body.sticky-bottom-footer {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

body.sticky-bottom-footer > .container.mt-5 {
  display: flex;
  flex-direction: column;
  flex: 1 0 auto;
}

body.sticky-bottom-footer > .container.mt-5 > .container-fluid {
  display: flex;
  flex-direction: column;
  flex: 1 0 auto;
}

/* Motto Section */
.motto-section {
  /* a true full-width footer: the top rule spans the page, echoing the
     header's line so the two frame the content */
  max-width: none;
  margin: 6rem 0 0;
  margin-top: auto;             /* absorb leftover viewport height — line sits at the very bottom */
  padding: 0.5rem 1rem 0.6rem;   /* a flat band — line, breath, text, done */
  border-top: 1px solid #e7e9ee;
  text-align: center;
}

.motto-container {
  position: relative;
  padding: 0;
}

.motto-quote {
  display: inline;   /* quote + attribution on one line */
  font-size: 0.8rem;
  font-weight: 300;
  color: #6b7280;   /* muted — footer furniture, not content */
  font-style: italic;
  line-height: 1.5;
  margin-bottom: 0;
  font-family: Georgia, serif;
  letter-spacing: 0;
}

.motto-attribution {
  display: inline;
  margin-left: 0.6rem;   /* small gap after the quote */
  font-style: italic;    /* fully uniform with the quote — no hierarchy */
  font-family: Georgia, serif;
  font-size: 0.8rem;     /* same size as the quote */
  color: #6b7280;        /* same color as the quote */
  margin-bottom: 0;
  font-weight: 300;
}



@media (max-width: 768px) {
  .motto-quote,
  .motto-attribution {
    font-size: 0.95rem;   /* keep quote + name the same size on mobile too */
  }

  /* on phones, drop the "— Haruki Murakami" to its own second line */
  .motto-attribution {
    display: block;
    margin-left: 0;
    margin-top: 0.35rem;
  }
  
  .motto-section {
    margin: 4rem 0 0;   /* full-width footer on mobile too, flush to the page end */
  }
}

/* ---- Posts layout: vertical filter sidebar + hairline divider (Cognition-style) ---- */
.posts-layout {
  display: flex;
  align-items: flex-start;
  gap: 0;
  max-width: 860px;
  width: 100%;
  margin: 1.5rem auto 14rem;   /* footer sits far below the content, at the very end of the scroll */
  padding: 0 1rem;
  position: relative;
}

/* Column rails: each starts with a bold tick flush against the header line
   (70px above this box) and runs a 1px hairline to the bottom of the section. */
.posts-layout::before,
.posts-layout::after {
  content: '';
  position: absolute;
  top: -70px;      /* reach up to the header's horizontal rule */
  bottom: 0;
  width: 2px;
  background:
    linear-gradient(#b3b8c2, #b3b8c2) 0 0 / 2px 14px no-repeat,
    linear-gradient(#e7e9ee, #e7e9ee) 0.5px 14px / 1px calc(100% - 14px) no-repeat;
}

.posts-layout::before {
  left: calc(1rem - 1px);              /* menu column rail */
}

.posts-layout::after {
  left: calc(4rem + 110px - 1px);      /* content column rail (menu 110px + 3rem air) */
}

.posts-filter {
  flex: 0 0 110px;
  margin-right: 3rem;    /* clear air between the menu column and the content rail */
  position: sticky;
  top: 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
  padding-top: 0;         /* menu starts level with the 01 marker */
  padding-left: 0.15rem;  /* text hugs the rail, evenly for every item */
}

.filter-item {
  appearance: none;
  background: none;
  border: none;
  padding: 0;
  margin: 0;
  position: relative;
  text-align: left;
  font-size: 0.95rem;
  font-weight: 400;
  color: #1a202c;
  cursor: pointer;
  line-height: 1.5;
  transition: color 0.15s ease;
}

.filter-item:hover {
  color: #1e3a8a;
}

/* kill the browser's default focus ring/box on click; keep it for keyboard nav */
.filter-item:focus {
  outline: none;
}

.filter-item:focus-visible {
  outline: 2px solid #2437e7;
  outline-offset: 2px;
}

.filter-item.is-active {
  color: #2437e7;   /* Cognition-style blue */
}

/* the "|" indicator floats just outside the rail, like Cognition's */
.filter-item.is-active::before {
  content: '';
  position: absolute;
  left: -0.5rem;   /* just off the rail */
  top: 0.32em;
  width: 3px;
  height: 0.78em;   /* matches the text's cap height, no taller */
  background: #2437e7;
}

.blog-list {
  /* wider than the title's ~600px so the reserved date column doesn't force
     titles to wrap early — line 1 stays long like the original */
  flex: 1 1 auto;
  min-width: 0;
  max-width: 700px;
  margin: 0;
  padding: 0 0 0 2rem;
  position: relative;   /* rail itself is drawn by .posts-layout::after */
}

/* a tiny mono section number hugging the rule, Cognition-style */
.blog-list::after {
  content: '01';
  position: absolute;
  top: 0;
  left: 0.35rem;
  font-family: 'SFMono-Regular', Menlo, Consolas, monospace;
  font-size: 0.5rem;   /* very small, Cognition-style */
  color: #b3b8c2;
  letter-spacing: 0.04em;
}

@media (max-width: 768px) {
  .posts-layout {
    flex-direction: column;
    gap: 1rem;
  }

  .posts-filter {
    position: static;
    flex-direction: row;
    align-items: baseline;   /* don't stretch buttons — keep the underline snug */
    gap: 1.25rem;
    padding-top: 0;
    padding-left: 0;
    border-left: none;
    margin-right: 0;
  }

  /* column furniture is a desktop-only device */
  .blog-list::before,
  .blog-list::after,
  .posts-layout::before,
  .posts-layout::after,
  .filter-item.is-active::before {
    display: none;
  }

  .filter-item {
    border-left: none;
    border-bottom: 2px solid transparent;
    padding: 0 0 0.25rem 0;
  }

  .filter-item.is-active {
    border-left: none;
    border-bottom: 2px solid #2437e7;
  }

  .blog-list {
    border-left: none;
    padding-left: 0;
  }
}

.blog-entry {
  display: flex;
  align-items: baseline;   /* date sits top-right, level with the title's first line */
  gap: 1.5rem;
  padding: 0.9rem 0;
  border-bottom: 1px solid #eef0f3;
}

.blog-entry .blog-title {
  flex: 1 1 auto;
  min-width: 0;   /* let the title wrap; it keeps ~600px so line 1 stays full */
}

.blog-entry:last-child {
  border-bottom: none;
}

.blog-date {
  order: -1;              /* date leads the row, Cognition-style */
  flex: 0 0 4.6rem;       /* fixed column so every title starts on the same rail */
  white-space: nowrap;
  font-family: 'SFMono-Regular', Menlo, Consolas, monospace !important;   /* same face as the 01 marker; beats override.css's span rule */
  font-size: 0.68rem;
  color: #9aa4b2;
  letter-spacing: 0.02em;
}

.blog-date.blog-soon {
  font-style: italic;
  color: #b8c0cc;
}

.blog-title {
  font-size: 1.08rem;
  font-weight: 500;
  color: #043976;   /* site dark blue, matches the Publications links */
  text-decoration: none !important;
  border-bottom: none !important;
  outline: none !important;
  line-height: 1.4;
  position: relative;
  display: inline-block;
  transition: color 0.2s ease;
}

/* Hover: no underline (the entry divider already draws a line) —
   light the whole row up in the accent blue, Cognition-style.
   Row-level hover so title and date change together. */
.blog-entry:hover .blog-title,
.blog-entry:hover .blog-date {
  color: #2437e7 !important;
}

.blog-date {
  transition: color 0.2s ease;
}

/* Remove underline from all link states */
.blog-title:link,
.blog-title:visited,
.blog-title:focus,
.blog-title:active {
  text-decoration: none !important;
  border-bottom: none !important;
  outline: none !important;
}

    /* Brand-blue text selection */
    ::selection { background: #2437e7; color: #fff; }
    ::-moz-selection { background: #2437e7; color: #fff; }
</style>

