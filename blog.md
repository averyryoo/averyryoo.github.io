---
layout: page
title: Blog
bg_image: /assets/images/bg-blog.jpg
---

{% for post in site.posts %}
- **[{{ post.title }}]({{ post.url }})**  
  <span class="post-date">{{ post.date | date: "%B %Y" }}</span>
{% endfor %}
