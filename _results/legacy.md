---
name: legacy
layout: newbase
---
{% include layouts/find_title.md name=page.name %}

{%- assign wwwURL="phenix/WWW/info/data" | relative_url -%}
{%- assign inspire="https://inspirehep.net/literature/" -%}
{%- assign hepdata="https://www.hepdata.net/record/ins" -%}
{%- assign hepdata_items=site.data.publications | where: "data","hepdata" -%}

{%- assign white_papers=site.data.publications | where: "data","whitepaper" -%}

##### The PHENIX White Paper

{%- for pub in  white_papers %}
* <a href="{{ inspire }}{{ pub.inspire }}" target="_blank">"{{ pub. title }}"</a>
{%- endfor %}


##### Top Cited Papers with HEPData entries

The following table contains links to **InspireHEP** and **HEPData** records
for select top cited PHENIX papers.
<table width="80%">
{%- for pub in  hepdata_items %}
<tr>
<td><b>{{ pub. title }}</b></td>
<td><a href="{{ inspire }}{{ pub.inspire }}" target="_blank">InspireHEP</a></td>
<td><a href="{{ hepdata }}{{ pub.inspire }}" target="_blank">HEPData</a></td>
</tr>
{%- endfor %}
</table>


{% comment %}
{%- for pub in  hepdata_items %}
* <a href="{{ inspire }}{{ pub.inspire }}" target="_blank">"{{ pub. title }}"</a>:&nbsp;<a href="{{ hepdata }}{{ pub.inspire }}" target="_blank">HEPData</a>
{%- endfor %}
{% endcomment %}