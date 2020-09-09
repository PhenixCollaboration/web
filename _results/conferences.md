---
name: conferences
layout: newbase
conferences:
- 'The 36th Winter Workshop on Nuclear Dynamics'
- 'Quark Matter 2019'
---
{% include layouts/find_title.md name=page.name %}

{% for conference in page.conferences %}
{%- include documents/doc.md category='physics' type='conference presentation' venue=conference -%}
{% endfor %}
