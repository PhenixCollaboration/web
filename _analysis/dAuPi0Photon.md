---
name: dAuPi0Photon
layout: newbase
---

<h3> Direct &#611; in d+Au collisions</h3>

The measurement of &gamma; and &pi;<sup>0</sup> yields in d+Au interactions is
important for studying the formation of quark-gluon plasma (QGP) in heavy ion
collisions.

One way to measure QGP formation is by observing jet suppression
using the nuclear modification factor R<sub>AB</sub>, which compares the yield of
a particle (in this case, the &pi;<sup>0</sup>) in AB collisions to that in p+p
collisions. R<sub>AB</sub> is calculated by dividing the invariant yield measured in
AB collisions by N<sub>coll</sub> times the invariant yield measured in p+p
collisions. If R<sub>AB</sub> is equal to one, then the yield observed in AB is the
same as that observed in p+p. If R<sub>AB</sub> is less than one, then the yield in AB
is suppressed, and if it is greater than one, then it is enhanced.

For a more detailed explanation that includes the motivation and physics
background, please refer to this [write-up]({{ '/assets/documents/dAuPi0Photon_intro.pdf' | relative_url }}).

{{ site.hr }}

* TOC
{:toc}

{{ site.hr }}

### About This Page

* This page is work in progress
* It is designed to capture the details of the analysis
of direct photons in d+Au collisions, with focus on the Electromagnetic Calorimeter
data.
* This analysis was performed by Dr. Niveditha Ramasubramanian
* The goal of this page is to consolidate information in a way that is sufficient
to make reproduction of this analysis possible.

---

### The Analysis Outline

#### General Analysis Workflow Diagram

&nbsp;

{% include images/image.md name='pi0_general' width=887 %}

---

#### The Original Code

A PHENIX-managed repository has been created on GitHub in order to capture the **original code**
(i.e. before adjustments were made to make it suitable for long-term preservation):
[https://github.com/PhenixCollaboration/emcal](https://github.com/PhenixCollaboration/emcal)

#### Input Data

Parts of this analysis use data samples kept in the storage area intended for long-term preservation.
This is its location in the GPFS filesystem of BNL SDCC:

```bash
/gpfs/mnt/gpfs02/phenix/data_preservation/phnxreco/emcal
```

#### Calibration Dependencies

There are "DeadWarn" and "Timing" type of maps which are prerequisite of this analysis
and they are considered as a separate "prior" component. In a condensed form, they
are preserved in the folder
[sim_Pi0Histogram/creatingHistogram_fromTTree](https://github.com/PhenixCollaboration/emcal/tree/master/sim_Pi0Histogram/creatingHistogram_fromTTree)
in the repository specified above.

---

### REANA

#### Setting up the Environment

REANA operates using containers. For the analysis presented here,
Docker images created by the PHENIX Collaboration are used. They are
hosted in a private registry maintained by the BNL SDCC. For the container
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


#### Running the Analysis with REANA

The REANA implementation of this analysis is based on the workflow diagram shown
above. To run this analysis within the REANA framework, certain adjustments had
to be made to the original code. The adjustments involve removing dependencies
on the batch system and creating workflow definitions that are native to REANA,
including staging the input data. We also made additional changes to improve the
code's readability, including renaming code units, functions, and scripts. You
can find the resulting code prepared for REANA in the `dAuPi0Photon` directory
of the PHENIX repository, available at
[https://github.com/PhenixCollaboration/reana](https://github.com/PhenixCollaboration/reana).

Each step of the analysis can be executed by using the corresponding workflow
defined in the YAML file. For example, to run the code in block `N`, issue the
following command in the terminal:

```bash
reana-client run -f N_reana.yaml -w N_reana
```

The input files will start uploading to the server, and you can check the job
status by pointing your browser to `$REANA_SERVER_URL`. Once the job is
complete, you can use the `reana-client` commands to list the files in the
workspace's working directory on the server and download the output results to
your local machine.

To list the files in the workspace's working directory on the server, use the
following command:

```bash
reana-client ls -w N_reana
```

To download the output results to your local machine, use the following command:

```bash
reana-client download -w N_reana path/to/output/file.dat
```

To select a specific set of files, you can combine the above commands using
Linux piping, for instance:

```bash
reana-client ls -w N_reana | grep output_plots/txt/ | cut -d' ' -f1 | xargs reana-client download -w N_reana
```

Finally, we provide further details below for each of the analysis steps
referenced by their "block numbers" defined in the analysis workflow diagram.


##### 1a. Raw &pi;<sup>0</sup> spectrum (MB + ERT)

The analysis starts with files produced by the *Taxi* process. The ROOT macro `pi0Extraction.cc` takes the *Taxi* ROOT files as input and generates `MB` (min bias)
and `ERT` (triggered) data as output. This macro is included in a driver script `corrPi0Chain.csh`.

```bash
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

```bash
# the original code found in the Condor submission part:
root -l -b <<EOF
  .L Pi0EmbedFiles.C
   Pi0EmbedFiles t
   t.Loop()
   EOF
```

Adaptation of the _ROOT_ macro for REANA, in a separate file *pi0run.script*:

```bash
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

```bash
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

```bash
reana-client download -w embed embedPi0dAu.tar
```

##### 3a. 2D response matrix of &pi;<sup>0</sup> momentum reconstruction

In this step we call a function in ROOT macro ``generationRM_Pi0.C`` that creates a set of ROOT
histograms. The histograms represent the response matrix (RM) for the &pi;<sup>0</sup> meson
production in heavy-ion collisions. The function reads an input ROOT file named ``EmbedPi0dAu.root``
and creates a new output ROOT file named ``Pion_RM.root``. The function calculates the RM by
dividing the Pt response (pTecore vs. generated Pt) for different centrality bins, particle
identification (PID), and detector sectors. The RM is stored in a 2D histogram (TH2D) with Pt bins.
The output response matrix represents the probability for a &pi;<sup>0</sup> particle with a given
generated momentum to be measured with a different momentum due to detector effects.

Tar file containing multiple ROOT files (see previous step `2a`) is uploaded as input for this step.
Abbreviated contents of driver script look as follows:

```bash
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

```bash
reana-client download -w gen Pion_RM.root
```

##### 5. Corrected &pi;<sup>0</sup> spectrum

This REANA step (final in this analysis)
is accomplished with scripts and macros named ```VConvolution_Pi0*```. The file ```Pion_RM.root```
serves as input, along with text files residing in ```output_plots``` previosly produced by the macros
```pi0extraction.C``` and ```WGRatio.C```:

```bash
scaledUEB_rawPi0_ERT_PbSc_0CC88_Chi2_3Sig.txt
scaledUEB_rawPi0_MB_PbSc_0CC88_Chi2_3Sig.txt
scaledUEB_rawPi0_BBCpERT_PbSc_0CC88_Chi2_3Sig.txt
````

The core of this step looks like this:

```bash
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
```bash
scaledEB_corrPi0_BBCpERT_PbSc_0CC88_Chi2_3Sig.txt
scaledUEB_corrPi0_BBCpERT_PbSc_0CC88_Chi2_3Sig.txt
```

Each of the following analysis steps can be performed using a dedicated REANA
workflow. For example, the user should be able to reproduce the results for step
X by creating and executing a workflow X_reana through the following commands:

```bash
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
