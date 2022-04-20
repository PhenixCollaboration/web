---
title: PHENIX membership
name: members
layout: newbase
---

{%- assign rows="" | split: "" -%}

### List of Active Members of the PHENIX Collabortion
<br/>

{% assign coll=site.data.collaboration | sort: "name" %}
{% for person in coll %}
{% assign name = person.name | split: "," %}
{% assign row="" | split: "" |push:name[0]|push:name[1]|push:person.email|push:person.inst %}
{% assign rows=rows | push: row %}
{% endfor %}

{% assign headers='Family Name,First Name,e-mail,Institution' | split:','%}
{% include layouts/table_versa.md headers=headers rows=rows width='120%' %}




{% comment %}
{% assign coll=site.data.collaboration | sort: "family_name" %}

{% for person in coll %}
{% assign row="" | split: "" |push:person.family_name|push:person.first_name|push:person.email|push:person.inst_name %}
{% assign rows=rows | push: row %}
{% endfor %}

{% assign headers='Family Name,First Name,e-mail,Institution' | split:','%}
{% include layouts/table_versa.md headers=headers rows=rows width='120%' %}

{% endcomment %}

