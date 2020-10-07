---
name: documents
layout: newbase

items:
   - {title: 'General Overviews',			category: 'overview',	type: 'document'}
   - {title: 'Beam Use Proposals',			category: 'detector',	type: 'bup'}
   - {title: 'Detector Subsystems (Writeups)',		category: 'detector',	type: 'writeup'}
   - {title: 'Detector Reference Papers',		category: 'detector',	type: 'publication'}
   - {title: 'Conference Presentations',		category: 'detector',	type: 'conference presentation'}
   - {title: 'Misc Summaries',				category: 'summary',	div: yes }

---
{% include layouts/find_title.md name=page.name %}

{% for item in page.items %}
{% if item.div %}<hr/>{% endif %}
{% include_cached documents/doc.md title=item.title category=item.category type=item.type %}
{% endfor %}
