---
title: PHENIX membership
name: members
layout: newbase
---

{% include title.md %}

{% assign rows="" | split: "" %}

##### Most recent list of active members of the PHENIX Collabortion
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

{% assign inst_name='' %}
{% for item in site.data.db.phenix_collab.institutional_affiliation %}
{% if item.person==person.id %}
{% for institution in site.data.db.phenix_collab.institutions %}
{% if institution.id==item.institute %}
{% assign inst_name=institution.name %}
{% break %}
{% endif %}
{% endfor %}


{% break %}
{% endif %}
{% endfor %}

{% assign row="" | split: "" %}
{% assign row=row|push:person.family_name|push:person.first_name|push:email|push:inst_name %}
{% assign rows=rows | push: row %}
{% endfor %}

{% assign headers="" | split: "" %}
{% assign headers=headers|push:'Family Name'|push:'First Name'|push:'e-mail'|push:'Institution' %}
{% include layouts/table_versa.md headers=headers rows=rows width='120%' %}
