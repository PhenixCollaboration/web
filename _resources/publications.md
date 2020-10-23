
name: publications
layout: newbase

items:
   - {title: 'PHENIX Systems',				category: 'systems',	type: 'publication'}


NOT USED, KEPT AS PLACEHOLDER

{% include layouts/find_title.md name=page.name %}

{% for item in page.items %}
{% if item.div %}<hr/>{% endif %}
{% include_cached documents/doc.md title=item.title category=item.category type=item.type %}
{% endfor %}

