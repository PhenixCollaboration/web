---
name: dAuPi0Photon
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
[https://github.com/PhenixCollaboration/emcal](https://github.com/PhenixCollaboration/emcal)

##### Input Data

Parts of this analysis use data samples kept in the storage area intended for long-term preservation.
This is its location in the GPFS filesystem of BNL SDCC:

```console
/gpfs/mnt/gpfs02/phenix/data_preservation/phnxreco/emcal
```

##### Calibration Dependencies

There are "DeadWarn" and "Timing" type of maps which are prerequisite of this analysis
and they are considered as a separate "prior" component. In a condensed form, they
are preserved in the folder
[sim_Pi0Histogram/creatingHistogram_fromTTree](https://github.com/PhenixCollaboration/emcal/tree/master/sim_Pi0Histogram/creatingHistogram_fromTTree)
in the repository specified above.

---

#### REANA

##### Setting up the Environment

REANA operates using containers. For the analysis presented here,
Docker images created by the PHENIX Collaboration are used. They are
hosted in a private registry maintained by the BNL SDCC. For the container
to work properly, a number of setup step are required, as listed below:

```csh
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
the script ```pi0extraction.csh```.

```yaml
version: 0.0.1
inputs:
  directories:
    - ./raw_taxiData
    - ./sim_Pi0Histogram
  files:
    - ./pi0extraction.C
    - ./WGRatio.C
    - ./generationRM_Pi0.C
    - ./VConvolution_Pi0.C
    - ./universal.h
    - ./setup_env.csh
    - ./pi0extraction.csh
workflow:
  type: serial
  specification:
    steps:
      - environment: 'registry.sdcc.bnl.gov/sdcc-fabric/rhic_sl7_ext:1.3'
        commands:
        - mkdir -p output_plots/pdf output_plots/txt output_plots/root
        - chmod +x ./pi0extraction.csh
        - ls -l > output.txt
        - ./pi0extraction.csh >> output.txt
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
the ROOT macro `pi0Extraction.cc` takes the *Taxi* ROOT files as input and generates `MB` (min bias)
and `ERT` (triggered) data as output. This macro is included in a driver script `corrPi0Chain.csh`.

##### Components

Below is an outline of the analysis sequence with references to "block numbers" in the
[workflow diagram](https://github.com/PhenixCollaboration/reana/blob/main/pi0extraction/sampleCode_correctedPi0.pdf){:target="_blank"},
along with pointers to relevant REANA components

##### 1a. Raw &pi;<sup>0</sup> spectrum (MB + ERT)

```console
# condor_Pi0Extraction.cc reformatted and renamed "pi0extraction.C"
root -l -b -q 'pi0extraction.C("MB", "PbSc", 4,5)'
root -l -b -q 'pi0extraction.C("ERT", "PbSc", 4,5)'
root -l -b -q 'WGRatio.C' # Merging MV and ERT spectra of raw pi0 with normalization

# The outputs of this step are placed in the output_plots folder,
# in three subfolders pdf, root, txt
```

These commands are included in ```pi0extraction.yaml```.
Currently a folder ```output_plots``` is created with subfolders ```txt,root,pdf```,
and the folder ```txt``` contains the actual analsys data.

##### 2a. &pi;<sup>0</sup> simulation

Presented below is the core of this workflow which includes processing of
multiple input files (60 in total):

```console
# the original code found in the Condor submission part:
root -l -b <<EOF
  .L Pi0EmbedFiles.C
   Pi0EmbedFiles t
   t.Loop()
   EOF
```

Adaptation of the _ROOT_ macro for REANA, in a separate file *pi0run.script*:

```console
gSystem->Load("libTHmul.so");
.L Pi0EmbedFiles.C
Pi0EmbedFiles t
t.Loop()
```

In the REANA script, this is used as follows: ```cat pi0run.script | root -b```.
Note that a PHENIX-specific ROOT library ```libTHmul.so``` is loaded
in the beginning, as this is necessary for proper operation of the macro.

Please refer to the
[relevant folder](https://github.com/PhenixCollaboration/reana/tree/main/pi0extraction/sim_Pi0Histogram){:target="_blank"}
in the PHENIX GitHub repository for access to the actual material.

This is the driver script ```Pi0EmbedFiles.csh```. Note that symbolic links are created
to feed successive files from a holding folder, to the _ROOT_ macro.

```csh
#!/bin/tcsh
source ./setup_env.csh

foreach i (`seq 0 1 $1`)
    ln -s gpfs/mnt/gpfs02/phenix/data_preservation/phnxreco/emcal/Pi0/test/simPi0_$i.root pi0_dAuMB.root
    echo File: $i
    ls -l pi0_dAuMB.root
    cat pi0run.script | root -b
    mv EmbedPi0dAu.root EmbedPi0dAu_$i.root
    rm pi0_dAuMB.root
end
tar -cf embedPi0dAu.tar EmbedPi0dAu_*
```

Processing of input files takes place sequentially and in this case takes a significant amount
of time compared to other steps, i.e. a feew hours.

The results of all emedding runs are bundled together in a _tar_ archive to make downloading easier. Upon
retrieval the data need to be merged using the utility ```haddPhenix``` which is done in block `3a` (see below).
Upon completion of this step the file ```embedPi0dAu.tar``` needs to be downloaded, and put
in the folder from where the next step is launched. An example of the cownload command, assuming the workflow
was named "embed":

```console
reana-client download -w embed embedPi0dAu.tar
```

##### 3a. 2D response matrix of &pi;<sup>0</sup> momentum reconstruction

The original macro ```generationRM_Pi0.cc``` was cleaned up (including removal of interactive graphics)
and renamed ```generationRM_Pi0.C```.

Tar file containing multiple ROOT files (see previous step `2a`) is uploaded as input for this step.
Abbreviated contents of driver script look as follows:

```csh
#!/bin/tcsh
source ./setup_env.csh
haddPhenix EmbedPi0dAu.root EmbedPi0dAu_*
root -l -b -q 'generationRM_Pi0.C'
```

The macro generates the file ```EmbedPi0dAu.root``` by merging inputs via ```haddPhenix```
and produces ```Pion_RM.root```. The complete description is in ```generationRM_Pi0.yaml```,
which resides with all subsidiary scripts in the folder ```generationRM```.

The workflow description is as follows:

```yaml
version: 0.0.1
inputs:
  files:
    - ./setup_env.csh
    - ./generationRM_Pi0.C
    - ./generationRM_Pi0.csh
    - ./embedPi0dAu.tar
workflow:
  type: serial
  specification:
    steps:
      - environment: 'registry.sdcc.bnl.gov/sdcc-fabric/rhic_sl7_ext:1.3'
        commands:
        - tar xvf embedPi0dAu.tar
        - chmod +x ./generationRM_Pi0.csh
        - ./generationRM_Pi0.csh > output.txt
        - ls -l >> output.txt

outputs:
  files:
    - output.txt
    - Pion_RM.root
```

The result will need to be downloaded as follows (assuming the worflow was assigned the name "gen" in REANA - can be anything):

```console
reana-client download -w gen Pion_RM.root
```

##### 5. Corrected &pi;<sup>0</sup> spectrum

This REANA step (final in this analysis)
is accomplished with scripts and macros named ```VConvolution_Pi0*```. The file ```Pion_RM.root```
serves as input, along with text files residing in ```output_plots``` previosly produced by the macros
```pi0extraction.C``` and ```WGRatio.C```:

```console
scaledUEB_rawPi0_ERT_PbSc_0CC88_Chi2_3Sig.txt
scaledUEB_rawPi0_MB_PbSc_0CC88_Chi2_3Sig.txt
scaledUEB_rawPi0_BBCpERT_PbSc_0CC88_Chi2_3Sig.txt
````

The core of this step looks like this:

```console
root -l -b -q 'VConvolution_Pi0.C'
```

The REANA submission file has this content:

```yaml
version: 0.0.1
inputs:
  directories:
    - ./output_plots
  files:
    - ./inputTrialFunction_Pi0.txt
    - ./setup_env.csh
    - ./VConvolution_Pi0.C
    - ./VConvolution_Pi0.csh
    - ./Pion_RM.root
workflow:
  type: serial
  specification:
    steps:
      - environment: 'registry.sdcc.bnl.gov/sdcc-fabric/rhic_sl7_ext:1.3'
        commands:
        - chmod +x ./VConvolution_Pi0.csh
        - ls -l > output.txt
        - ./VConvolution_Pi0.csh >> output.txt
        - ls -l >> output.txt

outputs:
  files:
    - output.txt0
```

Outputs are also written in ```output_plots/txt``` and contain
```console
scaledEB_corrPi0_BBCpERT_PbSc_0CC88_Chi2_3Sig.txt
scaledUEB_corrPi0_BBCpERT_PbSc_0CC88_Chi2_3Sig.txt
```

Each of the following analysis steps can be performed using a dedicated REANA
workflow. For example, the user should be able to reproduce the results for step
X by creating and executing a workflow X_reana through the following commands:

```console
cd reana/pi0extraction
reana-client run -w X_reana -f X_reana.yaml
```


##### 6. Corrected &eta; spectrum


##### 7. Decay &gamma; spectrum from &pi;<sup>0</sup>


##### 8. Decay &gamma; spectrum from &eta;, &eta;', and &Omega;


##### 9. Total decay &gamma; spectrum from &pi;<sup>0</sup>, &eta;, &eta;', and &Omega;


##### 10. Modified inclusive &gamma; spectrum


##### 11. Raw direct &gamma; spectrum


##### 12. Corrected direct &gamma; spectrum


##### 13. Direct &gamma; invariant yield


##### 14. &pi;<sup>0</sup> invariant yield
