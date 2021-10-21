---
name: emcal
layout: newbase
---

### Direct &#611; in d+Au collisions

{{ site.hr }}

* TOC
{:toc}

---

#### About

This page is work in progress and is designed to capture the details of the analysis
of direct photons in d+Au collisions, with focus on the Electromagnetic Calorimeter
data. The original analysis was performed by  Niveditha Ramasubramanian.

A repository has been created on GitHub in order to capture the original code:
[https://github.com/PhenixCollaboration/emcal](https://github.com/PhenixCollaboration/emcal){:target="_blank"}

General purpose storage area for this project, located in the filesystem of BNL SDCC:

```
/gpfs/mnt/gpfs02/phenix/data_preservation/phnxreco/emcal
```

---

#### REANA

##### The Code

In general,
{% include navigation/pagelink.md folder=site.analysis name='reana' tag='REANA' %}
implementation of this analysis follows 
[this partial diagram](https://github.com/PhenixCollaboration/reana/blob/main/pi0extraction/sampleCode_correctedPi0.pdf){:target="_blank"} of the analysis workflow.

In order for this analysis to run within the 
{% include navigation/pagelink.md folder=site.analysis name='reana' tag='REANA' %}
framework certain adjustments need to be made, such as removing dependencies
on the local batch system and creating workflow definitions native to REANA.
The code is kept in this PHENIX repository on GitHub (Work in Progress):
[https://github.com/PhenixCollaboration/reana/tree/main/pi0extraction](https://github.com/PhenixCollaboration/reana/tree/main/pi0extraction){:target="_blank"}

##### Notes
The following notes are referring to code and other materials contained in the repository mentioned above. Additional changes include occastional code cleanup and some minimal renaming of code units and functions to increase readability.

* Files produced by the Taxi process serve as input for this type of analysis
* The ROOT macro `pioExtraction.cc` takes the Taxi ROOT files as input and provides output for `MB` (min bias)
and `ERT` (triggered) data
* It is driven from the script `corrPi0Chain.csh`:

```bash
root -l -b -q 'pi0extraction.cc("MB", "PbSc", 4,5)'
root -l -b -q 'pi0extraction.cc("ERT", "PbSc", 4,5)'
root -l -b -q 'WGRatio.cc'

root -l -b -q 'generationRM_Pi0.cc'
root -l -b -q 'VConvolution_Pi0.cc'
```
* The outputs of this step are placed in the ```output_plots``` folder, in three subfolders `pdf`, `root`, `txt`