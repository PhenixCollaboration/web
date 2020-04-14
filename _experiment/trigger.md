---
title: Trigger Information
layout: newbase
abbrev: trigger
level: 0
weight: 30
document_folder: '/assets/documents/'
---

{% include title.md %}


#### EMCal/RICH trigger (ERT)
The EMCal/RICH trigger (ERT) selects events with high-p<sub>T</sub> electromagnetic probes or
the presence of heavy flavor decays.

#### References
{% assign items = site.data.documents %}
<ul>
{% for item in items %}
{% if item.tags contains 'ert' %}
<li><a href="{{ page.document_folder | append: item.name | relative_url }}" target="_blank">{{ item.title }}</a></li>
{% endif %}
{% endfor %}
</ul>

<hr/>
#### ERT Info
{% for run in site.data.runs %}

{% if run.ert_thresholds %}
<b>{{ run.run }}</b>: {{ run. ert_comment }}
{% include layouts/table.md headers='Date, Run, 4x4a, 4x4b, 4x4c, 2x2, RICH, Comment' rows=run.ert_thresholds width="100%" %}

{% if run.ert_notes %}
<b>Notes</b><br/>
{{ run.ert_notes }}
{% endif %}
<p/><br/>

<hr/>
{% endif %}


{% endfor %}

