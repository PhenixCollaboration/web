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
<table width="40%">
  <tr>
    <td width="55%"><h6><nobr>{{ conference.title }}</nobr></h6></td>
    <td width="30%"><h6>{{ link }}</h6></td>
    <td width="15%"><h6><a href="{{ conference.url }}" target="_blank">Conference website</a></h6></td>
  </tr>
</table>
{% endfor %}
<br/>
{% endfor %}
