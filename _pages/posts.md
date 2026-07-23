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

<div class="blog-list">
  <div class="blog-entry">
    <a href="/posts/c-guard/" class="blog-title">C-Guard: A Constitution-Grid Instrument for Data-Efficient RL Alignment</a>
    <span class="blog-date">Jul 2026</span>
  </div>

  <div class="blog-entry">
    <a href="https://x.com/lily_gpupoor/status/2076794330401087964" class="blog-title" target="_blank">My Take on the $100B Market for AI Training Data, Including RL Environments</a>
    <span class="blog-date">Jul 2026</span>
  </div>

  <div class="blog-entry">
    <a href="https://x.com/lily_gpupoor/status/2076114858203095503" class="blog-title" target="_blank">Second-Order Effects After Cursor and Cognition Cracked Post-Training</a>
    <span class="blog-date">Jul 2026</span>
  </div>

  <div class="blog-entry">
    <a href="https://x.com/lily_gpupoor/status/2074728312161849627" class="blog-title" target="_blank">Reflection: Where Is the Market for Post-Training as a Service?</a>
    <span class="blog-date">Jul 2026</span>
  </div>

  <div class="blog-entry">
    <a href="https://x.com/lily_gpupoor/status/2072083403898507278" class="blog-title" target="_blank">Poster @ AI Engineer World's Fair: Is Speculative Decoding All We Need?</a>
    <span class="blog-date">Jul 2026</span>
  </div>

  <div class="blog-entry">
    <a href="https://x.com/lily_gpupoor/status/2070401977251659794" class="blog-title" target="_blank">Build a Dense Reward for Your Writing</a>
    <span class="blog-date">Jun 2026</span>
  </div>

  <div class="blog-entry">
    <a href="/posts/code-is-all-you-need/" class="blog-title">Code Is All You Need: Reframing Feature Engineering as Code</a>
    <span class="blog-date">Jun 2026</span>
  </div>

  <div class="blog-entry">
    <a href="/posts/harbor-rlvr-environment/" class="blog-title">What Can't Be Measured Can't Be Solved: RLVR Environment Design from a Failure Taxonomy</a>
    <span class="blog-date">Jun 2026</span>
  </div>

  <div class="blog-entry">
    <a href="/posts/interaction-model/" class="blog-title">Thoughts on Thinking Machine's Interaction Model</a>
    <span class="blog-date">May 2026</span>
  </div>

  <div class="blog-entry">
    <a href="https://github.com/zarazhangrui/frontend-slides" class="blog-title" target="_blank">Frontend Slides: AI-Native Presentation Generation</a>
    <span class="blog-date">Apr 2026</span>
  </div>

  <div class="blog-entry">
    <a href="https://skill-claw.vercel.app/" class="blog-title" target="_blank">Skill Claw: Self-Improving Robot Agents</a>
    <span class="blog-date">Mar 2026</span>
  </div>

  <div class="blog-entry">
    <a href="https://supergeneral.vercel.app/" class="blog-title" target="_blank">SuperGeneral: Compositional Tool Environments for Agent Training</a>
    <span class="blog-date">Mar 2026</span>
  </div>

  <div class="blog-entry">
    <a href="https://sofagenius.ai/" class="blog-title" target="_blank">SofaGenius: Multi-Agent ML Research Assistant</a>
    <span class="blog-date">Feb 2026</span>
  </div>

  <div class="blog-entry">
    <a href="/posts/ieee-most-panel" class="blog-title">IEEE MOST Panel: Driving Force Towards Large-Scale AV Commercialization</a>
    <span class="blog-date">May 2025</span>
  </div>

  <div class="blog-entry">
    <a href="/posts/test-time-scaling" class="blog-title">Test Time Scaling</a>
    <span class="blog-date blog-soon">Coming soon</span>
  </div>

  <div class="blog-entry">
    <a href="/posts/contrastive-vs-generative-alignment" class="blog-title">Contrastive Alignment vs Generative Alignment</a>
    <span class="blog-date blog-soon">Coming soon</span>
  </div>
</div>

<style>
/* Header + nav come from the shared site CSS (main.css) via the splash layout,
   so this page matches Home and Papers exactly (background, zoom, header). */

/* Motto Section */
.motto-section {
  max-width: 700px;
  margin: 2rem auto 1.5rem;
  padding: 0 1rem;
  text-align: center;
}

.motto-container {
  position: relative;
  padding: 0;
}

.motto-quote {
  display: inline;   /* quote + attribution on one line */
  font-size: 1.25rem;
  font-weight: 300;
  color: #1a202c;
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
  font-size: 1.25rem;    /* same size as the quote */
  color: #1a202c;        /* same color as the quote */
  margin-bottom: 0;
  font-weight: 300;
}



@media (max-width: 768px) {
  .motto-quote,
  .motto-attribution {
    font-size: 1.125rem;   /* keep quote + name the same size on mobile too */
  }

  /* on phones, drop the "— Haruki Murakami" to its own second line */
  .motto-attribution {
    display: block;
    margin-left: 0;
    margin-top: 0.35rem;
  }
  
  .motto-section {
    margin: 2.5rem auto 3.5rem;
  }
}

.blog-list {
  /* wider than the title's ~600px so the reserved date column doesn't force
     titles to wrap early — line 1 stays long like the original */
  max-width: 700px;
  margin: 1.5rem auto 3rem;
  padding: 0 1rem;
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
  flex: 0 0 auto;
  margin-left: auto;   /* push the date to the far-right corner */
  white-space: nowrap;
  font-size: 0.85rem;
  color: #9aa4b2;
  letter-spacing: 0.01em;
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

.blog-title::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 1px;
  bottom: -2px;
  left: 0;
  background-color: #1e3a8a;
  visibility: hidden;
  transform: scaleX(0);
  transition: all 0.3s ease-in-out;
}

.blog-title:hover {
  color: #1e3a8a !important;
}

.blog-title:hover::after {
  visibility: visible;
  transform: scaleX(1);
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
</style>

