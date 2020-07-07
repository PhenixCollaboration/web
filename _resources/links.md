---
name: links
layout: newbase
items:
   - 'PHENIX website'
   - 'PHENIX Collaboration on GitHub'
   - 'PHENIX Community on Zenodo'
   - 'PHENIX on HEPData'
---
#### Links
{% for item in page.items %}
{%- include navigation/findlink.md name=item -%}
{% endfor %}

