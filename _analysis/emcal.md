---
name: emcal
layout: newbase
---
{% include layouts/find_title.md name=page.name %}

#### About

This page is work in progress and is designed to capture the details of the EMCAL analysis
performed by  Niveditha Ramasubramanian.
A repository has been created on GitHub in order to capture relevant code:
[https://github.com/PhenixCollaboration/emcal](https://github.com/PhenixCollaboration/emcal){:target="_blank"}

General purpose storage area for this project, located in the filesystem of BNL SDCC:

```
/gpfs/mnt/gpfs02/phenix/data_preservation/phnxreco/emcal
```

#### Notes

The following notes are referring to code and other materials contained in the repository mentioned above

* Files produced by the Taxi process serve as input for this type of analysis
* The ROOT macro `condor_Pi0Extraction.cc` takes the Taxi ROOT files as input and provides output for MB and ERT triggered dataset
* It is driven from the script `corrPi0Chain.csh`:

```bash
root -l -b -q 'condor_Pi0Extraction.cc("MB", "PbSc", 4,5)'
root -l -b -q 'condor_Pi0Extraction.cc("ERT", "PbSc", 4,5)'
root -l -b -q 'WGRatio.cc'

root -l -b -q 'generationRM_Pi0.cc'
root -l -b -q 'VConvolution_Pi0.cc'
```
* The outputs of this step are placed in the ```output_plots``` folder, in three subfolders `pdf`, `root`, `txt`