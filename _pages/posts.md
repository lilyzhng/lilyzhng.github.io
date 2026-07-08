---
layout: bare
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
  </div>
</div>

<div class="motto-section">
  <div class="motto-container">
    <div class="motto-quote">
      "Pain is inevitable but suffering is optional."
    </div>
    <div class="motto-attribution">
      — Haruki Murakami
    </div>

  </div>
</div>

<div class="blog-list">
  <div class="blog-entry">
    <a href="https://x.com/lily_gpupoor/status/2074728312161849627" class="blog-title" target="_blank">Reflection: Where Is the Market for Post-Training as a Service?</a>
    <span class="blog-date">Jul 2026</span>
  </div>

  <div class="blog-entry">
    <a href="https://x.com/lily_gpupoor/status/2072083403898507278" class="blog-title" target="_blank">Poster @ AI Engineer World's Fair: Is Speculative Decoding All We Need?</a>
    <span class="blog-date">Jun 2026</span>
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
    <a href="https://skill-claw.vercel.app/" class="blog-title" target="_blank">Skill Claw: Self-Debugging Robot Skill Agent</a>
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
/* Header Styling */
.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 2rem;
}

.name-container .author-name {
  font-size: 2rem;
  font-weight: 400;
  margin: 0;
  letter-spacing: -0.5px;
}

.navigation-container {
  display: flex;
  gap: 2rem;
}

.nav-link {
  font-size: 1.1rem;
  color: #4a5568;
  text-decoration: none;
  transition: color 0.2s ease;
}

.nav-link:hover {
  color: #2d3748;
}

/* Motto Section */
.motto-section {
  max-width: 700px;
  margin: 3rem auto 4rem;
  padding: 0 1rem;
  text-align: center;
}

.motto-container {
  position: relative;
  padding: 0;
}

.motto-quote {
  font-size: 1.25rem;
  font-weight: 300;
  color: #1a202c;
  font-style: italic;
  line-height: 1.5;
  margin-bottom: 0.5rem;
  font-family: Georgia, serif;
  letter-spacing: 0;
}

.motto-attribution {
  font-size: 0.875rem;
  color: #718096;
  margin-bottom: 0;
  font-weight: 400;
}



@media (max-width: 768px) {
  .header-container {
    flex-direction: column;
    gap: 1.5rem;
    margin: 1.5rem auto;
  }
  
  .name-container .author-name {
    font-size: 1.75rem;
  }
  
  .navigation-container {
    gap: 1.5rem;
  }
  
  .nav-link {
    font-size: 1rem;
  }
  
  .motto-quote {
    font-size: 1.125rem;
  }
  
  .motto-section {
    margin: 2.5rem auto 3.5rem;
  }
}

.blog-list {
  max-width: 600px;
  margin: 2rem auto 5rem;
  padding: 0 1rem;
}

.blog-entry {
  padding: 0.95rem 0;
  border-bottom: 1px solid #eef0f3;
}

.blog-entry:last-child {
  border-bottom: none;
}

.blog-date {
  display: block;
  margin-top: 0.3rem;
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
  color: #1a202c;
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

