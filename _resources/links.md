---
name: links
layout: newbase
items:
   - 'PHENIX website (legacy)'
   - 'PHENIX Collaboration on GitHub'
   - 'PHENIX Community on Zenodo'
   - 'PHENIX on HEPData'
   - 'PHENIX on Inspire'
---
#### Links
{% for item in page.items %}
{%- include navigation/findlink.md name=item category='general' %}
{% endfor %}
