---
name: emcal
layout: newbase
---

<h3> Direct &#611; in d+Au collisions</h3>

{{ site.hr }}

* TOC
{:toc}

---

#### About This Page

* This page is work in progress
* It is designed to capture the details of the analysis
of direct photons in d+Au collisions, with focus on the Electromagnetic Calorimeter
data.
* This analysis was performed by Dr. Niveditha Ramasubramanian
* The goal of this page is to consolidate information in a way that is sufficient
to make reproduction of this analysis possible.

#### The Analysis Outline

##### General Analysis Workflow Diagram

{% include images/image.md name='pi0_general' width=887 %}

---

##### The Original Code

A PHENIX-managed repository has been created on GitHub in order to capture the **original code**
(i.e. before adjustments were made to make it suitable for long-term preservation):
[https://github.com/PhenixCollaboration/emcal](https://github.com/PhenixCollaboration/emcal){:target="_blank"}

##### Input Data
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

##### Setting up the Environment

REANA operates using containers. For the analyses presented here,
Docker images created by the PHENIX Collaboration are used. They are
hosted in a private registry maintained the BNL SDCC. For the container
to work properly, a number of setup step are required, as listed below:

```bash
setenv OFFLINE_MAIN /cvmfs/phenix.sdcc.bnl.gov/x8664_sl7/release/release_new/new
setenv ONLINE_MAIN /cvmfs/phenix.sdcc.bnl.gov/x8664_sl7/release/release_new/new
setenv ROOTSYS /cvmfs/phenix.sdcc.bnl.gov/x8664_sl7/opt/phenix/core/root-5.34.36
setenv G4_MAIN /cvmfs/phenix.sdcc.bnl.gov/x8664_sl7/opt/phenix/core/geant4.10.00.p02

source /opt/phenix/core/stow/opt_phenix_scripts/bin/phenix_setup.csh

setenv LD_LIBRARY_PATH .:$LD_LIBRARY_PATH

setenv  ODBCINI ${PWD}/afs/rhic.bnl.gov/phenix/etc/odbc.ini
setenv PG_PHENIX_DBNAME Phenix_phnxdbrcf2_C
```
Since every line in the REANA submission file (formatted in YAML) has its own environment
the setup needs to be performed for every step that needs PHENIX-specific environment
variables. For this reasons the commands are often used with ```csh``` wrapper that
is reponsible for the setup. In the following example, ROOT macros are run from within
the script ```driver.csh```.

```yaml
version: 0.0.1
inputs:
  directories:
    - ./raw_taxiData
    - ./sim_Pi0Histogram
  files:
    - ./pi0extraction.cc
    - ./WGRatio.cc
    - ./generationRM_Pi0.cc
    - ./VConvolution_Pi0.cc
    - ./universal.h
    - ./setup_env.csh
    - ./driver.csh
workflow:
  type: serial
  specification:
    steps:
      - environment: 'registry.sdcc.bnl.gov/sdcc-fabric/rhic_sl7_ext:1.3'
        commands:
        - mkdir -p output_plots/pdf output_plots/txt output_plots/root
        - chmod +x ./driver.csh
        - ls -l > output.txt
        - ./driver.csh >> output.txt
        - ls -l >> output.txt

outputs:
  files:
    - output.txt
```



##### The Code

{% include navigation/pagelink.md folder=site.analysis name='reana' tag='REANA' %}
implementation of this analysis is based on the workflow illustrated in
[this partial diagram](https://github.com/PhenixCollaboration/reana/blob/main/pi0extraction/sampleCode_correctedPi0.pdf){:target="_blank"}.

In order for this analysis to run within the 
{% include navigation/pagelink.md folder=site.analysis name='reana' tag='REANA' %}
framework certain adjustments need to be made, such as
* Removing dependencies on the batch system
* Creating workflow definitions native to REANA including staging of the input data

Additional changes include some code cleanup and a minimal amount of renaming of code units, functions and scripts
for better readability.
The resulting code prepared for REANA is kept in this PHENIX repository on GitHub (Work in Progress):
[https://github.com/PhenixCollaboration/reana/tree/main/pi0extraction](https://github.com/PhenixCollaboration/reana/tree/main/pi0extraction){:target="_blank"}.

##### Starting Point

The analysis starts with files produced by the *Taxi* process. For example,
the ROOT macro `pioExtraction.cc` takes the *Taxi* ROOT files as input and generates `MB` (min bias)
and `ERT` (triggered) data as output. This macro is included in a driver script `corrPi0Chain.csh`.

##### Components

Below is an outline of the analysis sequence with references to "block numbers" in the
[workflow diagram](https://github.com/PhenixCollaboration/reana/blob/main/pi0extraction/sampleCode_correctedPi0.pdf){:target="_blank"}

##### Block 1
```bash
# Block 1
# condor_Pi0Extraction.cc reformatted and renamed "pi0extraction"
root -l -b -q 'pi0extraction.cc("MB", "PbSc", 4,5)'
root -l -b -q 'pi0extraction.cc("ERT", "PbSc", 4,5)'
root -l -b -q 'WGRatio.cc' # Merging MV and ERT spectra of raw pi0 with normalization

# The outputs of this step are placed in the output_plots folder,
# in three subfolders pdf, root, txt
```
##### Block 2

```bash
# Block 2, the original code found in the Condor submission part:
root -l -b <<EOF
  .L Pi0EmbedFiles.C
   Pi0EmbedFiles t
   t.Loop()
   EOF
```
Adaptation for REANA, in a separate file *pi0run.script*:
```bash
gSystem->Load("libTHmul.so");
.L Pi0EmbedFiles.C
Pi0EmbedFiles t
t.Loop()
```
In the REANA script, this is used as follows: ```cat pi0run.script | root -b```.
Note that a PHENIX-specific ROOT library ```libTHmul.so``` is loaded
in the beginning, as this is necessary for proper operation of the macro.

##### Block 3

```bash
# Block 3
root -l -b -q 'generationRM_Pi0.cc'
```

##### Block 4

```bash
# Block 4
root -l -b -q 'VConvolution_Pi0.cc'
```
