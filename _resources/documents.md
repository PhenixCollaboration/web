---
name: documents
layout: newbase

items:
   - {title: 'Beam Use Proposals',			category: 'detector',	type: 'bup'}
   - {title: 'Misc Summaries',				category: 'summary',	div: yes }

---
{% include layouts/find_title.md name=page.name %}

{% for item in page.items %}
{% if item.div %}<hr/>{% endif %}
{% include_cached documents/doc.md title=item.title category=item.category type=item.type %}
{% endfor %}
