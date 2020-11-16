---
name: conferences
layout: newbase
years:
- 2020
- 2019
- 2018
---
{% include layouts/find_title.md name=page.name %}

{% for year in page.years %}
{% assign c4y=site.data.conferences | where_exp: "item", "item.year==year" %}
<h5>{{ year }}</h5>
{% for conference in c4y %}
{% capture link %}{%- include navigation/zenodo_query.md name=conference.name tag='PHENIX Presentations' -%}{% endcapture %}
<table width="67%">
  <tr>
    <td width="65%"><nobr>{{ conference.title }}</nobr></td>
    <td width="25%"><nobr>{{ link }}</nobr></td>
    <td width="10%"><nobr><a href="{{ conference.url }}" target="_blank">Website</a></nobr></td>
  </tr>
</table>
{% endfor %}
<br/>
{% endfor %}
