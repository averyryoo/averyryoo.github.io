---
layout: page
title: research
bg_image: /assets/images/bg-research.jpg
permalink: /research
---

{% for paper in site.data.papers %}
<a class="paper-card" href="{{ paper.link }}" target="_blank" rel="noopener">
  <img src="{{ paper.image }}" alt="Paper thumbnail">
  <span class="paper-info">
    <span class="paper-title">{{ paper.title }}</span>
    <span class="paper-authors">{{ paper.authors }}</span>
    <span class="paper-venue">{{ paper.venue }}</span>
  </span>
</a>
{% endfor %}
