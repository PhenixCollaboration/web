---
name: conferences
layout: newbase
conferences:
- name: 'The 36th Winter Workshop on Nuclear Dynamics'
  abbrev: wwnd2020
- name: 'Quark Matter 2019'
  abbrev: qm2019
---
{% include layouts/find_title.md name=page.name %}

{% for conference in page.conferences %}
{%- include documents/doc.md category='physics' type='conference presentation' venue=conference.name -%}

{% include navigation/findlink.md name=conference.abbrev tag='Conference Website' %}
{{ site.hr }}
{% endfor %}
