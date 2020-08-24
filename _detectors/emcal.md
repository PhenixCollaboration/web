---
title: Electromagnetic Calorimeter
role: Electron and Photon identification
name: emcal
layout: newbase
category: central
---
{% include title.md %}

##### Write-ups
{% include documents/doc.md category='detector' type='writeup' tag='emcal' %}

##### Theses
{% include documents/doc.md category='detector' type='thesis' tag='emcal' %}

##### Publications
{% include documents/doc.md category='detector' type='publication' tag='emcal' %}
{% include documents/doc.md category='detector' type='preprint' tag='emcal' %}


{% comment %}
### Detector Overview
[PHENIX Electromagnetic Calorimeter (EMCal) – Detector Basics]({{ '/assets/detectors/emcal/emcal_shortdoc.pdf' | relative_url }})
{% endcomment %}


#### Variables and Accessors under PHCentralTrack Node (used for charged particle analyses)
{% include layouts/variables.md rows=site.data.emc.vars1 %}



#### Variables and Accessors under emcClusterContainer (used for neutral meson analyses)
EMCal has its own classes  `emcClusterContainer` and `emcClusterContent` that contain variables used mainly for the analysis of neutral mesons. The small code snippet below shows the usage of these classes and one example to access a variable. The rest of the variables listed below in the table can be accessed in the same manner.

```c++
PHCentralTrack* d_cnt = getClass<PHCentralTrack>(topNode,"PHCentralTrack");
emcClusterContainer *emccont = getClass<emcClusterContainer> (topNode, "emcClusterContainer");
emcClusterContent* emc = emccont->getCluster(icluster);
for ( unsigned int itrk = 0; itrk < d_cnt->get_npart(); ++itrk )
{
  for (int iclus = 0; iclus < int( emccont->size() ); iclus++)
   {
     emc = emccont->getCluster(iclus);
     float energy  = emc->ecore();
   }
 }
```
A complete list of these EMCal specific variables is as follows:
{% include layouts/variables.md rows=site.data.emc.vars2 %}
