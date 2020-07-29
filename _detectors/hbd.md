---
title: Hadron Blind Detector
role: Electron identification while being blind to hadrons
abbrev: hbd
name: hbd
layout: newbase
category: central
---
{% include layouts/find_detector_title.md abbrev=page.abbrev %}
## {{ title }}

{% assign items = site.data.documents %}

#### Introduction
The Hadron Blind Detector (HBD) was a conceptually novel Cherenkov
detector. Its primary aim was to recognize and reject tracks
originating from &pi;<sup>0</sup> Dalitz decays and gamma-conversions, thus
allowing to measure low mass
(m<sub>e<sup>+</sup>e<sup>-</sup></sub> &#8924;1GeV/c<sup>2</sup>)
electron-positron pairs produced in central Au+Au collisions at RHIC
energies. The main idea is to exploit the fact that the opening angle
of electron pairs from these sources is very small compared to pairs
from the vector mesons. The HBD was therefore located in a field-free
region, where the pair opening angle was preserved. The field free
region was created by an inner coil, installed in the central arms of
PHENIX. This coil counteracted the main field of the outer coils and
created an almost field-free region close to the vertex and extending
to &#8773;50-60 cm in the radial direction.

#### Detector Design
The Hadron Blind Detector was a windowless Cherenkov detector with a 50cm
long radiator operated with pure CF<sub>4</sub>, in a proximity focus
configuration. For an introduction to GEM detectors please see

{% include documents/doc.md category='detector' type='publication' tag='sauli_gem' %}

A triple GEM detector element avalanches
the photoelectrons produced in a 350nm CsI photocathode,
which is evaporated on the topmost Au plated GEM surface and
produce a blob on the pad readout plane. The use of CF<sub>4</sub> as a
radiator and detector gas in a windowless geometry results in a very
broad bandwidth (from 6 to 11.5 eV) and a very large figure of merit
(N<sub>0</sub>&#8765;800cm<sup>-1</sup>). A bias voltage is applied between the top
GEM and the mesh. Depending on the direction of the bias field, charge
produced by ionizing particles in the upper gap can either be
collected by the GEM (FB = Forward Bias)(right panel), or by the mesh
(RB = Reverse Bias)(left panel). In either configuration,
photoelectrons produced on the photocathode are collected with good 
efficiency into the GEM due to the strong electric field near the
holes. In the RB mode, only a very small amount of 
ionization charge produced very near the photocathode (within &#8765;150&mu;m)
is collected by the GEM. The FB mode is therefore sensitive
to hadrons and other charged particles, while the RB mode is
essentially sensitive only to the Cherenkov light produced by
electrons and hence the term "Hadron Blind". A comprehensive R&D
program was carried out to demonstrate the concept validity including
studies in the lab and also a beam test at KEK. The results are
published in the two NIM papers.
<!-- \cite{Nim1, Nim2}. -->

The design and construction of the detector vessel as well as assembly
and preliminary test of the GEM foils were carried out at the WIS whereas
$\it{CsI}$ evaporation, final assembly and test of detector modules were
done at the Stony Brook University. The analog and digital electronics
were developed and built by BNL Instrumentation and Columbia University.

#### Important HBD related Thesis/papers
{% include documents/doc.md category='detector' type='thesis' tag='naglis_thesis' %}
* [Deepali Sharma's Ph.D. Thesis](https://www.phenix.bnl.gov/phenix/WWW/talk/archive/theses/2010/Sharma_Deepali-thesis.pdf)  
* [Yosuke Watanable's Ph.D. Thesis](https://www.phenix.bnl.gov/phenix/WWW/talk/archive/theses/2014/Watanabe_Yosuke-phD_thesis_main.pdf)  

#### Detector Proposal
{% include documents/doc.md category='detector' type='proposal' tag='hbd' %}

#### Accessing HBD variables in the analysis
Work in progress

{% comment %}
An old style reference: ([sauli](https://www.sciencedirect.com/science/article/pii/S0168900296011722))
{% endcomment %}
