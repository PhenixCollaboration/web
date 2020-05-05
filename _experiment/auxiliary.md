---
title: Auxiliary Run Info
layout: newbase
abbrev: aux
name: aux
level: 0
weight: 1000
div: yes
---

## Run Chronology and Coordination

<table width="100%">
<tr><th>Run</th><th>Period</th><th>Coordinator(s)</th></tr>

{% for run in site.runs %}
{% include run/run_short.md run=run %}
{% endfor %}

</table>

## Misc Info

{% assign items = site.detectors | where: "abbrev", "run_configuration_gallery" %}
{% assign item=items[0] %}

<ul>
<li><a href="{{ item.url | relative_url }}">{{ item.title }} (graphics)</a></li>
<li><a href="{{ '/assets/documents/PHENIXSpin.pdf'| relative_url }}">Summary of the PHENIX Spin program (PDF)</a></li>
</ul>

<hr/>
{% include images/generic_gallery.md type="run_info" gallery="aux" title="Archived images of run summary tables (click for a larger image)" %}
<hr/>
