---
name: conferences
layout: newbase
years:
- 2021
- 2020
- 2019
- 2018
- 2017
- 2016
- 2015
---
{% include layouts/find_title.md name=page.name %}

{% for year in page.years %}
{% assign c4y=site.data.conferences | where_exp: "item", "item.year==year" | sort: "title" %}
<h5>{{ year }}</h5>
{% for conference in c4y %}
{% capture link %}{%- include navigation/zenodo_query.md name=conference.name tag='PHENIX Presentations' -%}{% endcapture %}
<table width="85%">
  <tr>
    <td width="65%"><nobr><a href="{{ conference.url }}" target="_blank">{{ conference.title }}</a></nobr></td>
    <td width="35%"><nobr>{{ link }}</nobr></td>
  </tr>
</table>
{% endfor %}
{{ site.hr }}
{% endfor %}
