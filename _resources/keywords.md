---
name: keywords
layout: newbase
---
{% include layouts/find_title.md name=page.name %}

Listed on this page are the keywords used to tag materials uploaded to the Zenodo sytem under the umbrella of the PHENIX Collaboration Community.
Each entry in the table below acts as a query link to Zenodo. Pages will open in a new tab/window.

{% assign rows="" | split: "" %}
{% assign sorted_keys=site.data.keywords | sort_natural %}

{% for item in sorted_keys %}

{% comment %}
{% assign link='<a href="http://cnn.com">' | append: item.name | append:'</a>' %}
{% endcomment %}
{% include navigation/zenodo_query.md name=item.name %}
{% assign row=link | append: ", " | append: item.description %}
{% assign rows=rows | push: row %}
{% endfor %}

{% include layouts/table.md headers='Keyword, Description' rows=rows %}
