---
title: Collaboration
name: collaboration
layout: newbase
---

{% include title.md %}

##### MGS20
---
{% assign mgsIDs = site.data.db.phenix_collab.mgs20 | map: "id" %}

{% assign mgsPeople="" | split: "" %}

{% for person in site.data.db.phenix_collab.people %}
{% if mgsIDs contains person.id %}
{% assign mgsPeople=mgsPeople | push: person %}
{% endif %}
{% endfor %}

{% assign mgsPeople=mgsPeople | sort: "family_name" %}

{% for person in mgsPeople %}
{% assign email='' %}
{% for item in site.data.db.phenix_collab.emailaddr %}
{% if item.person_id==person.id %}
{% assign email=item.email %}
{% break %}
{% endif %}
{% endfor %}

{{ person.family_name }}, {{ person.first_name }}, {{ email }}
{% endfor %}
