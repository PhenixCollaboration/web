---
title: Pad Chambers
name: pad_chambers
layout: newbase
category: central
---
{% include layouts/find_title.md name=page.name %}

#### Cross-section view of the PHENIX detector
<center>
{% include images/image.md name='x_sec_1' width=450 %}
</center>
<hr/>
#### Detector Overview
A detailed description about PHENIX Pad Chambers (PC) can be found at the following links. The PCs consist of three layers of multiwire proportional chambers, with a cathode pad readout. They provide space points along the trajectory of charged particles to determine the polar angle &theta; , used to calculate the p<sub>z</sub> component of the momentum vector.
PC1 is essential for the 3D momentum determination by providing the z-coordinate at the exit of the DC. The DC and PC1 information are combined to determine the straight line trajectories outside the magnetic field. PC2 and PC3 are needed to resolve ambiguities in the outer detectors where about 30% of the particles striking the EMCal are produced by either secondary interaction or decays outside the aperture of DC and PC1.

<hr/>
#### Theses
{% include documents/doc.md category='detector' type='thesis' tag='pad chamber' %}

<hr/>
#### Publications
{% include documents/doc.md category='detector' type='publication' tag='pad chamber' %}

#### Presentations
{% include documents/doc.md category='detector' type='presentation' tag='pad chamber' %}


<hr/>
#### Variables and Accessors under PHCentralTrack Node
{% include layouts/variables.md rows=site.data.pc.vars %}
