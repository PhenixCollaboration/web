---
title: Publications
abbrev: publications
name: publications
layout: newbase
weight: 0
items:
   - {title: 'General Overviews',			category: 'overview',	type: 'publication'}
   - {title: 'Detector Subsystems',			category: 'detector',	type: 'publication'}
   - {title: 'Data Reconstruction and Analysis',	category: 'dra',	type: 'publication'}
   - {title: 'PHENIX Systems',				category: 'systems',	type: 'publication'}
---
{% include title.md %}

{% for item in page.items %}
{% if item.div %}<hr/>{% endif %}
{% include documents/doc.md title=item.title category=item.category type=item.type %}
{% endfor %}

{% comment %}
{% include workinprogress.md %}
{% endcomment %}
