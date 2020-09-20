---
name: conferences
layout: newbase
conferences:
- name: wwnd2020
# - name: sfjhf20
- name: qm2019
---
{% include layouts/find_title.md name=page.name %}

{% for conference in page.conferences %}
{% assign item=site.data.conferences | where: "name", conference.name | first %}

{%- include navigation/zenodo_query.md name=item.name tag='PHENIX Presentations on Zenodo' -%}
{%- assign conference_website=site.data.links | where: "name", conference.name  | map: "url" | first -%}
<table width="100%">
  <tr>
    <td width="55%"><h4>{{ item.title }}</h4></td>
    <td width="10%"><h5><a href="{{ conference_website }}" target="_blank">Website</a></h5></td>
    <td width="35%"><h5>{{ link }}</h5></td>
  </tr>
</table>
<hr/>
{% assign detected=site.data.documents | where: "type", "conference presentation" | where: "venue", conference.name | size %}
{% if detected > 0%}
<center><h5>Select presentations</h5></center>
{% include documents/conference.md name=conference.name width='100%' %}
{% endif %}
{{ site.hr }}
{% endfor %}
