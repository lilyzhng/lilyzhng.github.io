---
layout: splash
title: "Thoughts"
permalink: /thoughts/
author_profile: true
---

<div class="header-container">
  <div class="name-container">
    <h1 class="author-name">Lily Zhang</h1>
  </div>
  <div class="navigation-container">
    <a href="/" class="nav-link">Home</a>
    <a href="/thoughts" class="nav-link">Thoughts</a>
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
    <a href="/thoughts/ieee-most-panel" class="blog-title">Reflections on IEEE MOST Panel: Driving Force Towards AV Commercialization</a><br>
    <span class="blog-author">Lily Zhang</span> - <span class="blog-date">5/5/25</span>
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
  max-width: 800px;
  margin: 3rem auto;
  padding: 0 1rem;
}

.blog-entry {
  margin-bottom: 2rem;
  line-height: 1.8;
}

.blog-author {
  font-size: 0.9rem;
  color: #666;
}

.blog-date {
  font-size: 0.9rem;
  color: #666;
}

.blog-title {
  font-size: 1.1rem;
  color: #1e3a8a;
  text-decoration: none !important;
  display: inline-block;
  margin-top: 0.2rem;
  position: relative;
  border-bottom: none !important;
  outline: none !important;
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
  color: #1e3a8a !important;
}

/* Ensure dark blue color in all states */
a.blog-title {
  color: #1e3a8a !important;
}

.blog-title:hover {
  color: #1e3a8a !important;
}
</style>

<!-- Visitor Counter -->
{% include visitor_counter_inline.html %}
