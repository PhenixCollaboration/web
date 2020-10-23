---
title: Beam Use Proposals
name: bup
layout: newbase

items:
   - {title: 'Decadal Plans', category: 'overview', type: 'decadal'}
   - {title: 'Beam Use Proposals', category: 'overview', type: 'bup'}

---
{% include layouts/find_title.md name=page.name %}

{% for item in page.items %}
{% if item.div %}<hr/>{% endif %}
{% include_cached documents/doc.md title=item.title category=item.category type=item.type %}
{% endfor %}
