---
layout: splash
title: ""
permalink: /
author_profile: true
---

# Lily Zhang

<!-- ░░░ Bio block with photo and links ░░░ -->
<div class="intro-flex">
  <div class="intro-left">          <!-- NEW wrapper -->
      <img src="/assets/img/prof_pic.jpg"
           alt="Lily Zhang"
           class="intro-avatar">
        <!-- social icons -->
        <div class="social-links">
          <a href="https://twitter.com/im_lilyz" aria-label="Twitter">
            <i class="fab fa-x-twitter"></i>
          </a>
          <a href="https://scholar.google.com/citations?user=la-Mx-UAAAAJ"
             aria-label="Google Scholar">
            <i class="ai ai-google-scholar"></i>
          </a>
          <a href="https://github.com/alchemz" aria-label="GitHub">
            <i class="fab fa-github"></i>
          </a>
          <a href="https://www.linkedin.com/in/alchemz/" aria-label="LinkedIn">
            <i class="fab fa-linkedin"></i>
          </a>
          <a href="mailto:alchemxz@gmail.com" aria-label="Email">
            <i class="fas fa-envelope"></i>
          </a>
        </div>
  </div>

  <div class="intro-text">
    <p>
      I am a Research Scientist at
      <a href="https://corporate.ford.com/operations/locations/silicon-valley.html" target="_blank" rel="noopener">Ford Autonomy</a>, Palo Alto, CA.
    </p>

    <p>
      At Ford, my research focuses on Perception and Prediction for autonomous driving tasks. I work on 3D perception, motion prediction, and geometric scene understanding.
    </p>

    <p>
      My research interests include scene relighting to improve the performance of SOTA CenterTrack algorithm, dataset bias identification using perceptual similarity based data clustering, and data augmentation via GANs for multiple autonomous driving tasks.
    </p>
    <p>
      My full name is Xianling Zhang.
    </p>
  </div>
</div>




## Invited Talks

<div id="talks-videos" class="video-grid">

<figure>
  <figcaption>Scene Relighting for Improved Object Detection</figcaption>
  <iframe
    src="https://www.youtube.com/embed/dQw4w9WgXcQ?playsinline=1&rel=0&mute=1"
    title="NVIDIA GTC 2023"
  ></iframe>
</figure>

<figure>
  <figcaption>Data Augmentation Techniques for Autonomous Driving</figcaption>
  <iframe
    src="https://www.youtube.com/embed/dQw4w9WgXcQ?playsinline=1&rel=0&mute=1"
    title="Stanford AI Lab"
  ></iframe>
</figure>

<figure class="video-item hidden">
  <figcaption>Addressing Dataset Bias in Machine Learning Models</figcaption>
  <iframe
    data-src="https://www.youtube.com/embed/dQw4w9WgXcQ?si=i3C3vljqV0AsVca6&mute=1"
    title="UC Berkeley EECS Department"
  ></iframe>
</figure>


<figure class="video-item hidden">
  <figcaption>The Future of Perception Systems in Autonomous Vehicles</figcaption>
  <iframe
    data-src="https://www.youtube.com/embed/dQw4w9WgXcQ?si=W7ZUtBpzK9X0xmix&mute=1"
    title="MIT CSAIL"
    loading="lazy"
  ></iframe>
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
  document.querySelectorAll(".more-button").forEach(btn => {
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