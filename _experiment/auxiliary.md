---
title: Auxiliary Run Info
layout: newbase
abbrev: aux
name: aux
level: 0
weight: 1000
div: yes
---
{% capture conf_gallery_url %}{%- include navigation/findpage.md folder=site.detectors name='run_configuration_gallery' -%}{% endcapture %}

#### Run Chronology and Coordination

<table width="100%">
<tr><th>Run</th><th>Period</th><th>Coordinator(s)</th></tr>

{% for run in site.runs %}
{% include run/run_short.md run=run %}
{% endfor %}

</table>
<hr/>
#### Misc Info

* [Run Configuration Gallery]({{ conf_gallery_url }})
{%- include documents/doc.md name='PHENIXSpin.pdf' category='summary' -%}

<hr/>
{% include images/generic_gallery.md type="run_info" gallery="aux" title="Archived images of run summary tables (click for a larger image)" %}
<hr/>
