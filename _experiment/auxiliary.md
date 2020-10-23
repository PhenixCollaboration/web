---
layout: newbase
name: aux
title: Misc Info
---
{% include layouts/find_title.md name=page.name %}
##### Run Chronology and Coordination

<table width="100%">
<tr><th>Run</th><th>Period</th><th>Coordinator(s)</th></tr>

{% for run in site.runs %}
{% assign run_record = site.data.runs | where: "run", run.run | first %}
{% assign run_title = run_record.title %}
{% assign run_coordinator = run_record.coordinator %}
{% assign run_period = run_record.period %}

<tr>
<td><a href="{{ run.url | relative_url }}">{{ run_title }}</a></td><td>{{ run_period }}</td><td>{{ run_coordinator }}</td>
</tr>
{% endfor %}

</table>
<hr/>

##### Run Configuration
{% include navigation/pagelink.md folder=site.detectors name='run_configuration_gallery' tag='Run Configuration Gallery' %}
##### Summaries
{%- include documents/doc.md category='summary' -%}

<hr/>
{% include images/generic_gallery.md type="run_info" gallery="aux" title="Archived images of run summary tables (click for a larger image)" %}
