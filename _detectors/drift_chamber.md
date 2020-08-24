---
title: Drift Chamber
name: drift_chamber
layout: newbase
category: central
---
{% include title.md %}

#### Cross-section view of the PHENIX detector
<center>
{% include images/image.md name='x_sec_1' width=450 %}
</center>
<hr/>
#### The frame of the Drift Chamber
<center>
{% include images/image.md name='dc-frame' width=450 %}
</center>
<hr/>
#### Detector Overview
The PHENIX drift chamber was a multiwire gaseous detector located at a radial distance of 2.02 &lt; R &lt; 2.48 m. There was one chamber on each arm, and they were mirror copies of each other, each one subtending 90<sup>&deg;</sup> in azimuth and 2 m along the z direction. The DC
measured the trajectories of charged particles in the r-&phi; plane in order to determine their charge and transverse momentum p<sub>T</sub> .
A detailed description about PHENIX Drift Chambers (DC) can be found in the following publication.


##### Publications
{% include documents/doc.md category='detector' type='publication' tag='drift chamber' %}


#### Variables and Accessors under PHCentralTrack Node
{% include layouts/variables.md rows=site.data.dch.vars %}
