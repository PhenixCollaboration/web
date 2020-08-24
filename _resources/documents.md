---
name: documents
layout: newbase

items:
   - {title: 'General Overviews',			category: 'overview',	type: 'document'}
   - {title: 'Beam Use Proposals',			category: 'detector',	type: 'bup'}
   - {title: 'Detector Subsystems (Writeups)',		category: 'detector',	type: 'writeup'}
   - {title: 'General References',			category: 'detector',	type: 'reference'}
   - {title: 'Select Theses',				category: 'detector',	type: 'thesis'}
   - {title: 'Misc Summaries',				category: 'summary',	div: yes }

---
{% include layouts/find_title.md name=page.name %}

{% for item in page.items %}
{% if item.div %}<hr/>{% endif %}
{%- include documents/doc.md title=item.title category=item.category type=item.type -%}
{% endfor %}
