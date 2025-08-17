---
layout: splash
title: ""
permalink: /
author_profile: true
---

<h1 class="centered-name">Lily Zhang</h1>


<!-- ░░░ Bio block with photo and links ░░░ -->
<div class="intro-flex">
  <div class="intro-left">          <!-- NEW wrapper -->
      <img src="/assets/img/prof_pic.jpg"
           alt="Lily Xianling Zhang"
           class="intro-avatar">
        <!-- social icons -->
        <div class="social-links">
          <a href="https://www.linkedin.com/in/alchemz/" aria-label="LinkedIn">
            <i class="fab fa-linkedin"></i>
          </a>
          <a href="https://github.com/alchemz" aria-label="GitHub">
            <i class="fab fa-github"></i>
          </a>
          <a href="https://scholar.google.com/citations?user=la-Mx-UAAAAJ" aria-label="Google Scholar">
            <i class="ai ai-google-scholar"></i>
          </a>
        </div>
  </div>

  <div class="intro-text">
    <p>
      I am a Research Scientist based in San Francisco / Bay Area, CA.
      <!-- I am a Research Scientist at
      <a href="https://corporate.ford.com/operations/locations/silicon-valley.html" target="_blank" rel="noopener">Ford Autonomy</a>, Palo Alto, CA. -->
    </p>

    <p>
      At Ford, my research focuses on Perception and Prediction for autonomous driving tasks. I work on 3D perception, motion prediction, and geometric scene understanding.
    </p>

    <p>
      My research interests include scene relighting to improve the performance of SOTA CenterTrack algorithm, dataset bias identification using perceptual similarity based data clustering, and data augmentation via GANs for multiple autonomous driving tasks.
    </p>
    <p>
      You can reach me at lilyzhng.ai AT gmail.com
    </p>
  </div>
</div>




## News

<div id="talks-videos" class="video-grid">
<figure>
  <figcaption>Hosting IROS 2025 RoboGen Workshop on 3D World Generation and Multimodal Reasoning<br><span class="venue-text">IEEE IROS 2025 Conferece</span></figcaption>
  <a href="https://robogen-iros.github.io/" target="_blank" rel="noopener" class="2025-iros-link">
    <img src="/assets/img/invited_talks/2025_iros.jpeg" alt="IROS Workshop" class="talk-thumbnail">
  </a>
</figure>

<figure>
  <figcaption>Chairing 2025 IEEE MOST Conference Panel Discussion<br><span class="venue-text">IEEE MOST 2025 Conferece</span></figcaption>
  <a href="https://ieeemobility.org/MOST2025/keynote.php" target="_blank" rel="noopener" class="2025-most-link">
    <img src="/assets/img/invited_talks/2025_most.png" alt="2025 MOST" class="talk-thumbnail">
  </a>
</figure>

<figure>
  <figcaption>Continuous Learning Loop: Online and Offline Perception<br><span class="venue-text">Presented at IROS Novel Sensor workshop and University of Delaware Seminar</span></figcaption>
  <iframe
    src="https://www.youtube.com/embed/_xMXiK9wBxE?playsinline=1&rel=0&mute=1"
    title="University of Delaware Lecture"
  ></iframe>
</figure>

<figure>
  <figcaption>Achieving AV Training Data Diversity Using AI Relighting<br><span class="venue-text">NVIDIA GTC Conference</span></figcaption>
  <a href="https://www.nvidia.com/en-us/on-demand/session/gtcspring23-s51407/" target="_blank" rel="noopener" class="nvidia-talk-link">
    <img src="/assets/img/invited_talks/2023_nvidia_2.png" alt="NVIDIA GTC Talk on Scene Relighting" class="talk-thumbnail">
    <div class="play-overlay">
      <i class="fas fa-circle-play"></i>
    </div>
  </a>
</figure>

<figure class="video-item hidden">
  <figcaption>Deep learning-based data-centric solutions.<br><span class="venue-text">Computer Vision Summit 2023</span></figcaption>
  <a href="https://computervisionsummit.com/location/cvsanjose/speaker/lilyxianlingzhang" target="_blank" rel="noopener" class="cv-summit-link">
    <img src="/assets/img/invited_talks/cv_summit_2023.png" alt="Computer Vision Summit 2023" class="talk-thumbnail">
  </a>
</figure>

<figure class="video-item hidden">
  <figcaption>Data misconceptions.<br><span class="venue-text">AI Accelerator Summit 2023</span></figcaption>
  <a href="https://www.researchgate.net/publication/382000139_Data_misconceptions_challenges_and_solutions" target="_blank" rel="noopener" class="cv-summit-link">
    <img src="/assets/img/invited_talks/ai_institude.png" alt="AI Accelerator Summit 2023" class="talk-thumbnail">
  </a>
</figure>

</div>

<button id="talks-more-button" class="more-button" data-target="#talks-videos">Show&nbsp;more</button>



---

## Papers

<ul id="papers-list" class="bibliography">
{% assign show_limit = 12 %}
{% for paper in site.data.papers %}
  <li{% if forloop.index0 >= show_limit %} class="hidden"{% endif %}>
    {% if paper.url %}
      <strong><a href="{{ paper.url }}" target="_blank" rel="noopener">{{ paper.title }}</a></strong><br>
    {% else %}
      <strong>{{ paper.title }}</strong><br>
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


<!-- put this at the very end of index.md (or whatever page),            -->
<!-- right before the closing markdown '---' or before any footer include -->
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