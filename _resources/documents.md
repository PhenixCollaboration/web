---
title: Documents
abbrev: documents
name: documents
layout: newbase
level: 0
weight: 10
items:
   - {title: 'General Overviews',			category: 'overview'}
   - {title: 'Detector Subsystems',			category: 'detector'}
   - {title: 'Data Reconstruction and Analysis',	category: 'dra'}
   - {title: 'PHENIX Systems',				category: 'systems'}
   - {title: 'Select Theses',				category: 'thesis'}
   - {title: 'Misc Summaries',				category: 'summary', div: yes }
---
{% include title.md %}

{% for item in page.items %}
{% if item.div %}<hr/>{% endif %}
{% include documents/doc.md title=item.title category=item.category %}
{% endfor %}
