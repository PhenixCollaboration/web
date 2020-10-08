---
name: conferences
layout: newbase
conferences:
- name: wwnd2020
- name: sfjhf20
- name: qm2019
- name: zs19
- name: dnp19
---
{% include layouts/find_title.md name=page.name %}

{% for conference in page.conferences %}
{% assign item=site.data.conferences | where: "name", conference.name | first %}

{%- include navigation/zenodo_query.md name=item.name tag='PHENIX Presentations on Zenodo' -%}
{%- assign conference_website=site.data.links | where: "name", conference.name  | map: "url" | first -%}
<table width="80%">
  <tr>
    <td width="50%"><h5><a href="{{ conference_website }}" target="_blank">{{ item.title }}</a></h5></td>
    <td width="50%"><h5>{{ link }}</h5></td>
  </tr>
</table>
{% endfor %}
