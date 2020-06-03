---
name: keywords
layout: newbase
---
{% include layouts/find_title.md name=page.name %}

{% assign rows="" | split: "" %}
{% assign sorted_keys=site.data.keywords | sort_natural %}

{% for item in sorted_keys %}
{% assign row=item.name | append: ", " | append: item.description %}
{% assign rows=rows | push: row %}
{% endfor %}

{% include layouts/table.md headers='Keyword, Description' rows=rows width="80%" %}
