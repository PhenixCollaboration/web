---
title: PHENIX membership
name: members
layout: newbase
---

{% include title.md %}

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

<table border="1">
<tr>
<th>Family Name</th><th>First Name</th><th>e-mail</th><th>Institution</th>
</tr>
  
{% for person in mgsPeople %}
<tr>
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

<td>{{ person.family_name }}</td><td>{{ person.first_name }}</td><td>{{ email }}</td><td>{{ inst_name }}</td>
</tr>
{% endfor %}
</table>
