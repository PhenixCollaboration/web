---
name: legacy
layout: newbase
---
{% include layouts/find_title.md name=page.name %}

{%- assign wwwURL="phenix/WWW/info/data" | relative_url -%}
{%- assign inspire="https://inspirehep.net/literature/" -%}
{%- assign hepdata="https://www.hepdata.net/record/ins" -%}


##### Top Cited Papers with HEPData entries

The following list contains links to InspireHEP records containing DOIs and other information
for select top cited PHENIX papers, with links to data packages published on the HEPData portal.

{% for pub in site.data.publications %}
* <a href="{{ inspire }}{{ pub.inspire }}" target="_blank">"{{ pub. title }}"</a>{% if pub.hepdata -%}:&nbsp;<a href="{{ hepdata }}{{ pub.inspire }}" target="_blank">HEPData</a>{%- endif -%}

{% endfor %}

##### Data Archive

At the time of writing, [HEPData]({% link _results/hepdata_policy.md %})
is the main tool for preserving data used in publications
and its use is mandated by the Collaboration.
Previously, the PHENIX Collaboration has kept publication-related
data (data points, tables etc) in a custom-built file-based
archive in various formats, most often as plain text files.


Since migration of the PHENIX Web site to a new type of service
such legacy data has become unavailable to users outside
of RHIC facilities. To mitigate this situation, portions
of these data are kept on this website in the original
format, on dedicated pages conforming to the
the original convention, so links previously disseminated
are still functional. Examples:

*  <a href="{{ wwwURL }}/ppg216_data.html" target="_blank">/phenix/WWW/info/data/ppg216_data.html</a> - <a href="https://inspirehep.net/literature/1672133" target="_blank">InspireHEP 1672133</a> - "Creation of quark–gluon plasma droplets with three distinct geometries"
*  <a href="{{ wwwURL }}/ppg217_data.html" target="_blank">/phenix/WWW/info/data/ppg217_data.html</a> - <a href="https://inspirehep.net/literature/1672014" target="_blank">InspireHEP 1672014</a> - "Nonperturbative transverse-momentum-dependent effects in dihadron and direct photon-hadron angular correlations in p+p collisions at s=√200 GeV"
* <a href="{{ wwwURL }}/ppg207_data.html" target="_blank">/phenix/WWW/info/data/ppg207_data.html</a> - <a href="https://inspirehep.net/literature/1632759" target="_blank">InspireHEP 1632759</a> - "Measurements of mass-dependent azimuthal anisotropy in central p+Au, d+Au, and <sup>3</sup>He+Au collisions at ​​√s<sub>NN</sub>=200 GeV"
* <a href="{{ wwwURL }}//ppg206_data.html" target="_blank">/phenix/WWW/info/data/ppg206_data.html</a> - <a href="https://inspirehep.net/literature/1610655" target="_blank">InspireHEP 1610655</a> - "Measurements of Multiparticle Correlations in d+Au Collisions at 200, 62.4, 39, and 19.6 GeV and p+Au Collisions at 200 GeV and Implications for Collective Behavior"