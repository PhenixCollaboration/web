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
<h4>{{ year }}</h4>
{% for conference in c4y %}
{% capture link %}{%- include navigation/zenodo_query.md name=conference.name tag='PHENIX Presentations' -%}{% endcapture %}
<table width="80%">
  <tr>
    <td width="40%"><h5>{{ conference.title }}</h5></td>
    <td width="30%"><h5>{{ link }}</h5></td>
    <td width="30%"><h5><a href="{{ conference.url }}" target="_blank">website</a></h5></td>
  </tr>
</table>
{% endfor %}
<br/>
{% endfor %}
