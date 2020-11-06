---
name: keywords
layout: newbase
categories:
- title: 'General'
  category: 'general'

- title: 'Conferences'
  category: 'conference'

- title: 'Physics'
  category: 'physics'

- title: 'Detector'
  category: 'detector'

- title: 'Simulation'
  category: 'simulation'

- title: 'PHENIX Runs'
  category: 'run'
---
{% include layouts/find_title.md name=page.name %}

Listed on this page are *recommended* keywords used to tag materials placed on this site
and also committed to cloud platforms such as 
{% include navigation/pagelink.md folder=site.results name='zenodo' tag='Zenodo'%}
(under the umbrella of the
{% include navigation/findlink.md name='PHENIX Community on Zenodo' %}),
and 
{% include navigation/findlink.md name='HEPData' %}.
They are critically important to make access to these resources efficient and PHENIX
materials readily discoverable, so their consistent
use strongly recommended. Keywords are also used in certain automated features of this site. 

**The keywords are case-sensitive.** We adopted lowercase convention for all keywords for
the following reason: Zenodo is using a complex query mechanism which includes "elastic search"
so the effect of capitalization on queries is not always straighforward, so it's best to avoid
ambiguity. Note that Zenodo keywords can actually be a combination of words and white space
(i.e. phrases). Multiple such combinations are allowed in a single query when accessing Zenodo.

In the tables below, the keywords are grouped in categories. Each entry in the left
column acts as a query link to *Zenodo*, for that specific keyword. Pages containing
results of queries will open in a new tab/window.

{% for cat in page.categories %}
{% if cat.title %}
  <br/>

{% assign rows="" | split: "" %}
{% assign sorted_keys=site.data.keywords | where: "category", cat.category | sort_natural %}
##### {{ cat.title }} ({{ sorted_keys.size }} items)

{% for item in sorted_keys %}

{% capture link %}{%- include navigation/zenodo_query.md name=item.name -%}{% endcapture %}
{% assign row=link | append: ", " | append: item.description %}
{% assign rows=rows | push: row %}
{% endfor %}

{% include layouts/table.md headers='Keyword, Description' widths='30%,70%' width='60%' rows=rows %}
{% endif %}
{% endfor %}
