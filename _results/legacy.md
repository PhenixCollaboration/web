---
name: legacy
layout: newbase
---
{% include layouts/find_title.md name=page.name %}

{%- assign wwwURL="phenix/WWW/info/data" | relative_url -%}
{%- assign inspire="https://inspirehep.net/literature/" -%}
{%- assign hepdata="https://www.hepdata.net/record/ins" -%}
{%- assign hepdata_items=site.data.publications | where: "data","hepdata" -%}
{%- assign legacy_items=site.data.publications | where: "data","legacy" -%}

##### Top Cited Papers with HEPData entries

The following list contains links to **InspireHEP** records containing DOIs and other information
for select top cited PHENIX papers, with links to data packages published on the HEPData portal.

{%- for pub in  hepdata_items %}
* <a href="{{ inspire }}{{ pub.inspire }}" target="_blank">"{{ pub. title }}"</a>:&nbsp;<a href="{{ hepdata }}{{ pub.inspire }}" target="_blank">HEPData</a>
{%- endfor %}

##### Data Archive

At the time of writing,
{% include navigation/pagelink.md folder=site.results name='hepdata_policy' tag='HEPData' %}
is the main platform for preserving data included in publications (such as in plots and tables)
and its use is mandated by the Collaboration. It is recommended that when trying to locate
numerical data for a particular publicaiton that portal is consulted first, using the InspireHEP
ID of the publication as the key.

Previously, the PHENIX Collaboration has kept publication-related
data in a custom-built file-based
archive in various formats, most often as plain text files. Creation
of equivalent HEPData entries is underway, but is not complete.
Since the migration of the PHENIX Web site to a new type of service
in 2020 such legacy data has become unavailable to users outside
of RHIC facilities. To mitigate this situation, portions
of these data are kept on this website in the original
format, on dedicated pages conforming to the
the original convention, such that the links like posted below
are still functional.

{%- for pub in  legacy_items %}
* <a href="{{ inspire }}{{ pub.inspire }}" target="_blank">"{{ pub. title }}"</a>:&nbsp;<a href="{{ wwwURL }}/{{ pub.legacyURL }}" target="_blank">{{ pub.legacyURL }}</a>
{%- endfor -%}

