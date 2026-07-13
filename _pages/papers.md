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

## Publications

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


---

## Service

<ul id="service-list">
  <li>
    <span class="service-title">Program Committee Member</span><br>
    TPC for NeurIPS ('21, '24, '25), CVPR ('22, '23, '24, '25), ICRA ('23), IROS ('23), ICML ('23), ICLR ('24), ECCV ('24),  KDD ('24), ICCV ('25)
  </li>
  
  <li>
    <span class="service-title">Industry Advisory Board <a href="https://www.linkedin.com/feed/update/urn:li:activity:7265427014088556546/">[MXET Board Meeting]</a></span><br>
    Invited to serve on the Industry Advisory Board at Texas A&M University 
  </li>
  
  <li>
    <span class="service-title">Journal Editor <a href="https://dl.acm.org/journal/tiot/calls-for-papers">[Call for Papers]</a></span><br>
    Invited guest editor for ACM Journal, Transactions on Internet of Things, Special Issue on Autonomous Driving
  </li>

  
  <li>
    <span class="service-title">Conference Chair <a href="https://ieeemobility.org/MOST2025/keynote.php">[Keynote & Panel]</a>, <a href="https://docs.google.com/presentation/d/1yAV6jGk2n1CLgnNpIYc4ORwTF69NOKmQ6u0fDyX9f_0/edit?slide=id.p#slide=id.p">[Slides]</a></span><br>
    Chairing for The IEEE International Conference on Mobility (MOST) Panel Discussion "Driving Force: Towards Large-Scale Autonomous Driving Commercialization"
  </li>
  
  <li>
    <span class="service-title">Workshop Moderator <a href="https://docs.google.com/presentation/d/1i6EZEfebDGI1I0zpZoV6OHZ5kWvmX3OZ/edit?usp=sharing&ouid=103941006958426062861&rtpof=true&sd=true">[Slides]</a></span><br>
    Moderated the "Generative AI: A New World Simulator to Transform data generation at large scale" workshop at the Auto.AI conference
  </li>
  
  <li>
    <span class="service-title">Hackathon Judge</span><br>
    Invited judge for Gen AI Hackathon in San Francisco
  </li>
</ul>

{% raw %}
<script>
/* unified handler from previous message */
document.addEventListener("DOMContentLoaded", () => {
  // Hide 'Show more' buttons if there are no hidden items
  document.querySelectorAll(".more-button").forEach(btn => {
    const target = document.querySelector(btn.dataset.target);
    if (target && target.querySelectorAll(".hidden").length === 0) {
      btn.style.display = 'none';
    }
    
    btn.addEventListener("click", () => {
      const target = document.querySelector(btn.dataset.target);
      if (!target) return;

      target.querySelectorAll(".hidden").forEach(fig => {
        fig.classList.remove("hidden");
        const ifr = fig.querySelector("iframe[data-src]");
        if (ifr) ifr.src = ifr.dataset.src;
      });

      btn.remove();
    });
  });
});
</script>
{% endraw %}
