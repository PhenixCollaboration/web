---
name: emcal
layout: newbase
---

<h3> Direct &#611; in d+Au collisions</h3>

{{ site.hr }}

* TOC
{:toc}

---

#### Analysis Outline

##### General Analysis Workflow Diagram

{% include images/image.md name='pi0_general' width=887 %}

##### Preservation of original code and input data

This page is work in progress and is designed to capture the details of the analysis
of direct photons in d+Au collisions, with focus on the Electromagnetic Calorimeter
data. The original analysis was performed by  Niveditha Ramasubramanian.
A PHENIX-managed repository has been created on GitHub in order to capture the original code:
[https://github.com/PhenixCollaboration/emcal](https://github.com/PhenixCollaboration/emcal){:target="_blank"}

Parts of this analysis use data samples kept in the storage area intended for long-term preservation.
This is its location in the GPFS filesystem of BNL SDCC:

```bash
/gpfs/mnt/gpfs02/phenix/data_preservation/phnxreco/emcal
```

##### Calibration Dependencies
There are "DeadWarn" and "Timing" type of maps which are prerequisite of this analysis
and they are considered as a separate "prior" component. In a condensed form, they
are preserved in the folder
[sim_Pi0Histogram/creatingHistogram_fromTTree](https://github.com/PhenixCollaboration/emcal/tree/master/sim_Pi0Histogram/creatingHistogram_fromTTree){:target="_blank"}
in the repository specified above.

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
The code created for use in REANA is kept in this PHENIX repository on GitHub (Work in Progress):
[https://github.com/PhenixCollaboration/reana/tree/main/pi0extraction](https://github.com/PhenixCollaboration/reana/tree/main/pi0extraction){:target="_blank"}.
Additional changes include some code cleanup and a minimal amount of renaming of code units, functions and scripts
for better readability.

##### Starting Point

The analysis starts with files produced by the *Taxi* process. For example,
the ROOT macro `pioExtraction.cc` takes the *Taxi* ROOT files as input and generates `MB` (min bias)
and `ERT` (triggered) data as output. This macro is included in a driver script `corrPi0Chain.csh`.

##### Components

Below is an outline of the analysis sequence with references to "blocks" in the
[workflow diagram](https://github.com/PhenixCollaboration/reana/blob/main/pi0extraction/sampleCode_correctedPi0.pdf){:target="_blank"}

```bash
# Block 1
root -l -b -q 'pi0extraction.cc("MB", "PbSc", 4,5)'
root -l -b -q 'pi0extraction.cc("ERT", "PbSc", 4,5)'
root -l -b -q 'WGRatio.cc'
# The outputs of this step are placed in the output_plots folder,
# in three subfolders pdf, root, txt


# Block 2
# NB. This is where a parallel workflow needs to be implemented
# This is the payload which runs in the inner loop:
root -l -b <<EOF
  .L Pi0EmbedFiles.C
   Pi0EmbedFiles t
   t.Loop()
   EOF


# Block 3
root -l -b -q 'generationRM_Pi0.cc'

# Block 4
root -l -b -q 'VConvolution_Pi0.cc'
```
