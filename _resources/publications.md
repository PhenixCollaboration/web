---
name: publications
layout: newbase

items:
   - {title: 'General Overviews',			category: 'overview',	type: 'publication'}
   - {title: 'Data Reconstruction and Analysis',	category: 'dra',	type: 'publication'}
   - {title: 'PHENIX Systems',				category: 'systems',	type: 'publication'}
---

{% include layouts/find_title.md name=page.name %}

{% for item in page.items %}
{% if item.div %}<hr/>{% endif %}
{% include_cached documents/doc.md title=item.title category=item.category type=item.type %}
{% endfor %}

