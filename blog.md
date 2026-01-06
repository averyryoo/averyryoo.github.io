---
layout: page
title: blog
bg_image: /assets/images/bg-blog.jpg
permalink: /blog
---

{% for post in site.posts %}
- **[{{ post.title }}]({{ post.url }})**  
  <span class="post-date">{{ post.date | date: "%B %Y" }}</span>
{% endfor %}
