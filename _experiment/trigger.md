---
title: Trigger Information
layout: newbase
name: trigger
---

{% include title.md %}


#### EMCal/RICH trigger (ERT)
The EMCal/RICH trigger (ERT) selects events with high-p<sub>T</sub> electromagnetic probes or
the presence of heavy flavor decays.

#### References
{% include documents/doc.md category='detector' tag='ert' %}
{% include documents/doc.md category='physics' tag='ert' %}



<hr/>
#### ERT Info
{% for run in site.data.runs %}

{% if run.ert_thresholds %}
##### {{ run.run | replace: "run", "Run " }}
{{ run. ert_comment }}
{% include layouts/table.md headers='Date, Run, 4x4a, 4x4b, 4x4c, 2x2, RICH, Comment' rows=run.ert_thresholds width="100%" %}
{% if run.ert_notes %}
<p/>
<b>Notes</b><br/>
{{ run.ert_notes }}
{% endif %}
{% if run.ert_masks %}
<b>Masks</b><br/>
{% include layouts/table.md headers='Date, Run, Download Link, DB, Comment' rows=run.ert_masks width="100%" download='download' %}
{% endif %}
<hr/>
<hr/>
{% endif %}


{% endfor %}

