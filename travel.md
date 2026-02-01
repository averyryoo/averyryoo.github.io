---
layout: page
title: places i've been
bg_image: /assets/images/bg-travel.jpg
permalink: /travel
---

<p><strong>{{ site.data.travel.size }}</strong> countries visited. Click on a highlighted country to see photos from that trip.</p>

<div id="travel-map" class="travel-map-container"></div>

{% include travel-modal.html %}

<script>
  // Inject travel data from Jekyll
  window.travelData = [
    {% for country in site.data.travel %}
    {
      code: "{{ country.code }}",
      name: "{{ country.name }}",
      year: {{ country.year | default: "null" }},
      photos: [{% for photo in country.photos %}"{{ photo }}"{% unless forloop.last %}, {% endunless %}{% endfor %}],
      caption: "{{ country.caption | default: '' }}"
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];
</script>
<script src="/assets/js/travel-map.js"></script>
