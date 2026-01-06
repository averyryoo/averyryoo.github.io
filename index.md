---
layout: default
title: home
bg_image: /assets/images/bg-index.jpg
---

<div class="hero">
  <img src="/assets/images/headshot.png" class="headshot" alt="Headshot">

  <div>
    <h1>avery (hee-woon) ryoo 🦖</h1>
    <p class="subtitle">PhD Student @ Mila + Université de Montréal</p>
    <p>
      I am a CS PhD student at Mila - Quebec AI Institute and the Université de Montréal, where I work with Guillaume Lajoie and Matt Perich.
    </p>
    <p>
      I am primarily interested in deep generative models -- especially their applications in medicine and science. I aim to use ideas from deep learning, compositionality, and dynamical systems theory to design generative frameworks that are faster and more sample-efficient — a crucial step in mitigating the widening resource disparity in an era of increasingly large models.
    </p>
    <p>
      In another life, I studied biomedical engineering at the University of Waterloo, during which I completed several internships in data science, computer vision research, and brain-computer interfaces.
    </p>
  </div>
</div>

<div class="social-block">
  <div class="social-links" aria-label="Social links">
    <a class="social-link email" href="{{ site.social.email }}" aria-label="Email">
      <svg class="social-icon" viewBox="0 0 24 24" aria-hidden="true">
        <rect x="3" y="5" width="18" height="14" rx="2.2" ry="2.2"></rect>
        <path d="M4 7.5 12 12.5 20 7.5"></path>
        <path d="M4 17l4.5-3.2"></path>
        <path d="M20 17 15.5 13.8"></path>
      </svg>
    </a>

    <a class="social-link twitter" href="{{ site.social.twitter }}" aria-label="Twitter / X" target="_blank" rel="noreferrer">
      <img class="social-icon-img" src="/assets/images/icons/twitter.png">
    </a>

    <a class="social-link bluesky" href="{{ site.social.bluesky }}" aria-label="Bluesky" target="_blank" rel="noreferrer">
      <img class="social-icon-img" src="/assets/images/icons/bluesky.png">
    </a>

    <a class="social-link scholar" href="{{ site.social.scholar }}" aria-label="Google Scholar" target="_blank" rel="noreferrer">
      <img class="social-icon-img" src="/assets/images/icons/scholar.png">
    </a>

    <a class="social-link linkedin" href="{{ site.social.linkedin }}" aria-label="LinkedIn" target="_blank" rel="noreferrer">
      <img class="social-icon-img" src="/assets/images/icons/linkedin.png">
    </a>
  </div>
</div>

{% include news.html %}
