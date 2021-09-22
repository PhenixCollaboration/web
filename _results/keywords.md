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

- title: 'Software and Computing'
  category: 'software'

- title: 'Data and Analysis Preservation'
  category: 'dap'

- title: 'PHENIX Runs'
  category: 'run'
---
{% include layouts/find_title.md name=page.name %}

Listed on this page are *recommended* keywords used for two purposes:
* to **tag materials** placed on this site so they can be consistently referenced across this web resource
* to enhance discoverability of the PHENIX materials committed to {% include navigation/pagelink.md folder=site.results name='zenodo' tag='Zenodo'%}

Consistent use of the keywords is strongly recommended. Please note that
{% include navigation/pagelink.md folder=site.results name='hepdata_instructions' tag='HEPData materials' %}
follow a 
{% include navigation/findlink.md name='hepdata_keywords' tag='different set of conventions' %}.


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

{% include layouts/table.md headers='Keyword, Description' widths='30%,70%' width='100%' rows=rows %}
{% endif %}
{% endfor %}
