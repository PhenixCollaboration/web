---
name: conferences
layout: newbase
conferences:
- name: wwnd2020
- name: qm2019
---
{% include layouts/find_title.md name=page.name %}

{% for conference in page.conferences %}
{% include documents/conference.md name=conference.name %}

{{ site.hr }}
{% endfor %}
