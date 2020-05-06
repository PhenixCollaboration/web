---
title: Time-of-Flight
role: Measures the position of charged particles. Identifies particles.
abbrev: tof
layout: newbase
category: central
---
{% include title.md %}




#### Detector overview
The TOF
(sometimes called the TOFE to contrast with the TOFW)
is a time-of-flight (TOF) detector in the east (E) arm of the PHENIX central
spectrometer.  It was designed, developed, and assembled at Tsukuba University.  It was
part of the original design of PHENIX and was successfully operated for all 16 run
periods.

The individual component of the TOFE is the slat.  Each slat is a plastic scintillation
counter made of Bicron BC404 read out on either end with a Hamamatsu R3478S
photomultiplier tube.

The TOFE system consists of 10 panels.  Each panel contains 96 slats for a total of 960
slats and 1920 readout channels.  There are eight panels in sector 1 covering the full
22.5 degrees in azimuth and the full +/- 0.35 units in pseudorapidity, and two panels in
sector 0 covering full 22.5 degrees in azimuth and the innermost rapidity range.



#### Archived papers
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3766511.svg)](https://doi.org/10.5281/zenodo.3766511)
[Felix Matathias's Ph.D. Thesis (gzipped postscript)](https://www.phenix.bnl.gov/phenix/WWW/talk/archive/theses/2004/Matathias_Felix-thesis.ps.gz)



#### Variables and Accessors
These “get” methods give access to the TOFW variables used for analysis. The variable type, name of the get method, and a brief description are given below.

{% include layouts/variables.md rows=site.data.tof.vars %}


