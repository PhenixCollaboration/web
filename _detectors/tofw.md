---
abbrev: tofw
layout: newbase
category: central
---
{% include layouts/find_detector_title.md abbrev=page.abbrev %}
## {{ title }}

#### Intro
The TOFW is a time-of-flight (TOF) detector in the west (W) arm of the PHENIX central
spectrometer.  It was designed, developed, and assembled at Vanderbilt University with
Julia Velkovska as the project lead.  It was installed prior to the beginning of Run7
and was successfully operated for all running periods thereafter.

#### MRPC
The individual component of the TOFW detector is the mult-gap resistive plate chamber
(MRPC).  Each MRPC has six 230 micron gaps separated by glass plates.  The gaps are filled
with a gas mixture.

* During the commissioning run in 2007 (Run7), the gas mixture was 95%
R134a (1,1,1,2-Tetrafluoroethane) and 5% isobutane (2-Methylpropane).
* In the 2008 operational period (Run8) the gas mixture was changed to 95% R134a, 4.5% isobutane,
and 0.5% sulfur hexafluoride (SF6).
* Starting in the operational period in 2011 (Run11), the gas mixture was changed to 92%
R134a, 5% isobutane, and 3% SF6.

At either side (longitudinally) of the gaps are electrodes held at +/- 7 kV for a total
potential difference of 14 kV across the gaps.  Outside of the electrodes on either side
(longitudinally) are sets of four copper strips that are read out on either side, for a
total of 8 readout channels per MRPC.  When charged particles cross the gap, the gas is
ionized.  The charge in the gas is imaged in the strips.  The induced charge in the strips
is read out on either end (transversely).  Each strip is about 37 cm long and 2.8 cm wide.
The lengthwise location of the hit in the strip is determined via the difference in time
on either end.  Since the strip is only 1 inch wide, the widthwise location of the hit is
taken to be the center of the strip.

#### The System
The TOFW system consists of four boxes.  Each box subtends 11.5 degrees in azimuth and
0.35 units in pseudorapidity.  There are two boxes in sector 1 and two boxes in sector 2,
with each sector receiving full coverage in pseudorapidity and half coverage in azimuth.
Each box has four high voltage busses in two rows.  Each high voltage buss powers 8 MRPCs,
for a total of 32 per box and 128 total, meaning there are 1024 readout channels in total.

#### Archived papers

{% assign items = site.data.documents %}

##### Write-ups
{% include documents/doc.md title=item.title category='detector' type='writeup' tag='tofw' %}

##### Theses
{% include documents/doc.md category='detector' type='thesis' tag='brian_love_thesis' %}
{% include documents/doc.md category='detector' type='thesis' tag='hugo_valle_thesis' %}
{% include documents/doc.md category='detector' type='thesis' tag='ron_belmont_thesis' %}

#### Variables and Accessors
These “get” methods give access to the TOFW variables used for analysis. The variable type, name of the get method, and a brief description are given below.

{% include layouts/variables.md rows=site.data.tofw.vars %}

{% comment %}
<!-- [PHENIX Time-of-flight detector West (TOFW) – Detector Basics]({{ '/assets/detectors/tofw/tofw_shortdoc.pdf' | relative_url }}) -->
* [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3836478.svg)](https://doi.org/10.5281/zenodo.3836478) [Brian Love's M.S. Thesis](https://www.phenix.bnl.gov/phenix/WWW/talk/archive/theses/2009/Love_Brian-thesis_BrianLove.pdf)  
* [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3836538.svg)](https://doi.org/10.5281/zenodo.3836538) [Hugo Valle's Ph.D. Thesis](https://www.phenix.bnl.gov/phenix/WWW/talk/archive/theses/2008/Valle_Hugo-thesisHugoValle.pdf)  
* [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3836568.svg)](https://doi.org/10.5281/zenodo.3836568) [Ron Belmont's Ph.D. Thesis](https://www.phenix.bnl.gov/phenix/WWW/talk/archive/theses/2012/Belmont_Ron-belmont.pdf)  

{% endcomment %}
