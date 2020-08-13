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


#### Variables and Accessors under PHCentralTrack Node (used for charged particle analyses)
{% include layouts/variables.md rows=site.data.emc.vars1 %}



#### Variables and Accessors under emcClusterContainer (used for neutral meson analyses)
To use these variables one needs to define an object; emccont = findNode::getClass<emcClusterContainer> (topNode, "emcClusterContainer"; and then you loop over all the clusters in a clusterContainer and define
another object emcClusterContent emc=emccont->getCluster(icluster) to access the variables for a given cluster

{% include layouts/variables.md rows=site.data.emc.vars2 %}
