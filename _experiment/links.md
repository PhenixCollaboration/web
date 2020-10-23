---
name: links
layout: newbase
items:
   - 'PHENIX on Inspire'
   - 'PHENIX on HEPData'
   - 'PHENIX Community on Zenodo'
   - 'PHENIX Collaboration on GitHub'
---
{% include layouts/find_title.md name=page.name %}

{% for item in page.items %}
{%- include navigation/findlink.md name=item category='general' %}
{% endfor %}
