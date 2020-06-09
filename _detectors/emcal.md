---
title: Electromagnetic Calorimeter
role: Electron and Photon identification
abbrev: emcal
layout: newbase
category: central
---
{% include layouts/find_detector_title.md abbrev=page.abbrev %}
## {{ title }}


{% assign items = site.data.documents %}

##### Write-ups
{% include documents/doc.md category='detector' type='writeup' tag='emcal' %}

##### Theses
{% include documents/doc.md category='detector' type='thesis' tag='emcal' %}


{% comment %}
### Detector Overview
A detailed description about Electromagentic Calorimeter (EMCal) can be found in the write-up linked below.

[PHENIX Electromagnetic Calorimeter (EMCal) – Detector Basics]({{ '/assets/detectors/emcal/emcal_shortdoc.pdf' | relative_url }})
{% endcomment %}

#### Variables and Accessors
{% include layouts/variables.md rows=site.data.emc.vars %}
