---
name: keywords
layout: newbase
---
{% include layouts/find_title.md name=page.name %}
{% capture zenodo_page_url %}{% include navigation/findpage.md folder=site.resources name='zenodo' %}{% endcapture %}

Listed on this page are *recommended* keywords used to tag materials used on this site.
Keywords are used in certain automated features i.e. aggregation and linking of materials
pertaining to a particular topic, so their consistent use is definitely enouraged.

Importantly, same uniform set of keywords is used for materials uploaded to the
[Zenodo]({{ zenodo_page_url }}) sytem under the umbrella of the
{% include navigation/phenix_zenodo_collection.md %}. The list is compiled
to provide better consistency of the subsequent queries. Zenodo is using a complex
query mechanism which includes but is not limited to "elastic search" on the submission
text (where applicable) so the effect of capitalization on queries is not always straighforward.
In the following we adopt lowercase convention for all keywords. Note that "keywords" on Zenodo
can actually be combination of words (i.e. phrases), space-separated.

Each entry in the left column of the table below acts as a query link to *Zenodo*. Pages will open in a new tab/window.

{% assign rows="" | split: "" %}
{% assign sorted_keys=site.data.keywords | sort_natural %}

{% for item in sorted_keys %}

{% include navigation/zenodo_query.md name=item.name %}
{% assign row=link | append: ", " | append: item.description %}
{% assign rows=rows | push: row %}
{% endfor %}

{% include layouts/table.md headers='Keyword, Description' rows=rows %}
