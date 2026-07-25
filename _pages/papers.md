---
layout: splash
title: "Lily Zhang | Papers"
permalink: /papers/
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
  <nav class="posts-filter" aria-label="Section filter">
    <button class="filter-item is-active" data-filter="publications">Publications</button>
    <button class="filter-item" data-filter="service">Service</button>
  </nav>

  <div class="blog-list" data-section="01">
  <div class="section-group" data-group="publications">
<ul id="papers-list" class="bibliography">
{% assign show_limit = 6 %}
{% for paper in site.data.papers %}
  <li{% if forloop.index0 >= show_limit %} class="hidden"{% endif %}>
    {% if paper.url %}
      <strong><a href="{{ paper.url }}" target="_blank" rel="noopener">{{ paper.title }}</a></strong>
      {% if paper.project_url %}
        <a href="{{ paper.project_url }}" target="_blank" rel="noopener" class="project-link">[Project Page]</a>
      {% endif %}
      {% if paper.code_url %}
        <a href="{{ paper.code_url }}" target="_blank" rel="noopener" class="code-link">[Code]</a>
      {% endif %}<br>
    {% else %}
      <strong>{{ paper.title }}</strong>
      {% if paper.project_url %}
        <a href="{{ paper.project_url }}" target="_blank" rel="noopener" class="project-link">[Project Page]</a>
      {% endif %}
      {% if paper.code_url %}
        <a href="{{ paper.code_url }}" target="_blank" rel="noopener" class="code-link">[Code]</a>
      {% endif %}<br>
    {% endif %}
    {{ paper.authors }}.<br>

    {% if paper.venue or paper.year %}
      <cite>
        {% if paper.venue %}{{ paper.venue }}{% endif %}
        {% if paper.volume %} {{ paper.volume }}{% endif %}
        {% if paper.pages  %}, {{ paper.pages }}{% endif %}
        {% if paper.year   %} ({{ paper.year }}){% endif %}
      </cite>
    {% endif %}
  </li>
{% endfor %}
</ul>

<button id="papers-more-button"
        class="more-button"
        data-target="#papers-list">
  Show&nbsp;more
</button>
  </div><!-- /.section-group publications -->

  <div class="section-group" data-group="service" hidden>
<ul id="service-list">
  <li>
    <span class="service-title">Program Committee Member</span><br>
    TPC for NeurIPS ('21, '24, '25), CVPR ('22, '23, '24, '25), ICRA ('23), IROS ('23), ICML ('23), ICLR ('24), ECCV ('24),  KDD ('24), ICCV ('25)
  </li>

  <li>
    <span class="service-title">Industry Board Advisor for Texas A&M University</span><br>
    Invited to serve on the Industry Advisory Board at Texas A&M University <a href="https://www.linkedin.com/feed/update/urn:li:activity:7265427014088556546/">[MXET Board Meeting]</a>
  </li>

  <li>
    <span class="service-title">Industry Board Advisor for University of Delaware</span><br>
    Supporting young researchers and shaping strategic directions for the CAR Robotics Lab
  </li>

  <li>
    <span class="service-title">ACM Journal Editor</span><br>
    Invited guest editor for ACM Journal, Transactions on Internet of Things, Special Issue on Autonomous Driving <a href="https://dl.acm.org/journal/tiot/calls-for-papers">[Call for Papers]</a>
  </li>

  <li>
    <span class="service-title">IEEE Conference Chair</span><br>
    Chairing for The IEEE International Conference on Mobility (MOST) Panel Discussion "Driving Force: Towards Large-Scale Autonomous Driving Commercialization" <a href="https://ieeemobility.org/MOST2025/keynote.php">[Keynote & Panel]</a>, <a href="https://docs.google.com/presentation/d/1yAV6jGk2n1CLgnNpIYc4ORwTF69NOKmQ6u0fDyX9f_0/edit?slide=id.p#slide=id.p">[Slides]</a>
  </li>

  <li>
    <span class="service-title">IEEE IROS Workshop Chair</span><br>
    Moderated the "Generative AI: A New World Simulator to Transform data generation at large scale" workshop at the Auto.AI conference <a href="https://docs.google.com/presentation/d/1i6EZEfebDGI1I0zpZoV6OHZ5kWvmX3OZ/edit?usp=sharing&ouid=103941006958426062861&rtpof=true&sd=true">[Slides]</a>
  </li>

  <li>
    <span class="service-title">Hackathon Judge</span><br>
    Invited judge for Gen AI Hackathon in San Francisco
  </li>
</ul>
  </div><!-- /.section-group service -->
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

{% raw %}
<script>
document.addEventListener('DOMContentLoaded', function () {
  // Section switcher (Publications / Service), mirrors the /posts/ filter
  var buttons = document.querySelectorAll('.posts-filter .filter-item');
  var groups = document.querySelectorAll('.section-group');
  var list = document.querySelector('.blog-list');
  var sectionNumbers = { publications: '01', service: '02' };
  function apply(f) {
    groups.forEach(function (g) { g.hidden = (g.getAttribute('data-group') !== f); });
    if (list) list.setAttribute('data-section', sectionNumbers[f] || '01');
  }
  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      buttons.forEach(function (b) { b.classList.remove('is-active'); });
      btn.classList.add('is-active');
      apply(btn.getAttribute('data-filter'));
    });
  });
  apply('publications');   // Publications is the default view

  // 'Show more' handler for the publications list
  document.querySelectorAll('.more-button').forEach(function (btn) {
    var target = document.querySelector(btn.dataset.target);
    if (target && target.querySelectorAll('.hidden').length === 0) {
      btn.style.display = 'none';
    }
    btn.addEventListener('click', function () {
      var target = document.querySelector(btn.dataset.target);
      if (!target) return;
      target.querySelectorAll('.hidden').forEach(function (el) { el.classList.remove('hidden'); });
      btn.remove();
    });
  });
});
</script>
{% endraw %}

<style>
/* Pin the footer to the viewport bottom when the (filtered) list is short */
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

/* Motto footer */
.motto-section {
  max-width: none;
  margin: 6rem 0 0;
  margin-top: auto;
  padding: 0.5rem 1rem 0.6rem;
  border-top: 1px solid #e7e9ee;
  text-align: center;
}
.motto-container { position: relative; padding: 0; }
.motto-quote {
  display: inline;
  font-size: 0.8rem;
  font-weight: 300;
  color: #6b7280;
  font-style: italic;
  line-height: 1.5;
  margin-bottom: 0;
  font-family: Georgia, serif;
  letter-spacing: 0;
}
.motto-attribution {
  display: inline;
  margin-left: 0.6rem;
  font-style: italic;
  font-family: Georgia, serif;
  font-size: 0.8rem;
  color: #6b7280;
  margin-bottom: 0;
  font-weight: 300;
}

/* Section groups: only the active one shows */
.section-group[hidden] { display: none; }

/* ---- Same two-rail layout as /posts/ : filter menu + content column ---- */
.posts-layout {
  display: flex;
  align-items: flex-start;
  gap: 0;
  max-width: 860px;
  width: 100%;
  margin: 1.5rem auto 14rem;
  padding: 0 1rem;
  position: relative;
}
.posts-layout::before,
.posts-layout::after {
  content: '';
  position: absolute;
  top: -70px;
  bottom: 0;
  width: 2px;
  background:
    linear-gradient(#b3b8c2, #b3b8c2) 0 0 / 2px 14px no-repeat,
    linear-gradient(#e7e9ee, #e7e9ee) 0.5px 14px / 1px calc(100% - 14px) no-repeat;
}
.posts-layout::before { left: calc(1rem - 1px); }
.posts-layout::after  { left: calc(4rem + 110px - 1px); }

.posts-filter {
  flex: 0 0 110px;
  margin-right: 3rem;
  position: sticky;
  top: 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
  padding-top: 0;
  padding-left: 0.15rem;
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
  font-family: 'Cormorant Garamond', 'EB Garamond', serif;
}
.filter-item:hover { color: #1e3a8a; }
.filter-item:focus { outline: none; }
.filter-item:focus-visible { outline: 2px solid #2437e7; outline-offset: 2px; }
.filter-item.is-active { color: #2437e7; }
.filter-item.is-active::before {
  content: '';
  position: absolute;
  left: -0.5rem;
  top: 0.32em;
  width: 3px;
  height: 0.78em;
  background: #2437e7;
}

.blog-list {
  flex: 1 1 auto;
  min-width: 0;
  max-width: 700px;
  margin: 0;
  padding: 0 0 0 2rem;
  position: relative;
}
.blog-list::after {
  content: attr(data-section);
  position: absolute;
  top: 0;
  left: 0.35rem;
  font-family: 'SFMono-Regular', Menlo, Consolas, monospace;
  font-size: 0.5rem;
  color: #b3b8c2;
  letter-spacing: 0.04em;
}

@media (max-width: 768px) {
  .posts-layout { flex-direction: column; gap: 1rem; }
  .posts-filter {
    position: static;
    flex-direction: row;
    align-items: baseline;
    gap: 1.25rem;
    padding-top: 0;
    padding-left: 0;
    margin-right: 0;
  }
  .blog-list::after,
  .posts-layout::before,
  .posts-layout::after,
  .filter-item.is-active::before { display: none; }
  .filter-item {
    border-bottom: 2px solid transparent;
    padding: 0 0 0.25rem 0;
  }
  .filter-item.is-active { border-bottom: 2px solid #2437e7; }
  .blog-list { padding-left: 0; }

  .motto-quote, .motto-attribution { font-size: 0.95rem; }
  .motto-attribution { display: block; margin-left: 0; margin-top: 0.35rem; }
  .motto-section { margin: 4rem 0 0; }
}
</style>
