---
name: software_overview
layout: newbase
---
{% include layouts/find_title.md name=page.name %}

##### Foundation software and platforms
The PHENIX software history and its evolution covers approximately 30 years. Two frameworks form its foundation:
* PISA: simulation framework based on Geant 3
* fun4all: reconstruction and analysis framework. Motivated by neccessity of integrating of code developed independently for many subsystems and bring it under one umbrella

The official  operating system for PHENIX is Redhat Scientific Linux. This is the operating system installed on the machines in {% include navigation/findlink.md name='sdcc' tag='BNL SDCC' %} (Scientific Data And Computing Center). The official shell supported is `csh` and its varieties like `tcsh`. Since certain parts of calibrations and conditions-type data are available within the file system mounted on these machines they effectively represent the only location where meaningful production and analysis can be performed.

PHENIX relies mainly on {% include navigation/findlink.md name='cvs' tag='CVS'  %} for version control.
Some components of the software (e.g. analysis) utilize a set of build tools which include 
{% include navigation/findlink.md name='automake' -%},
{% include navigation/findlink.md name='autoconf' -%},
{% include navigation/findlink.md name='libtool' -%}.

##### Containers
For produciton, PHENIX relies on containerization to maintain a stable computing environment (SL6-bases) which exists for a long period of time, which helps ensure complete reproducibility of results (e.g. DSTs) at the bit level. At the time of writing, containers are not used in analysis.

##### Standard Login Scripts and Software Directories
Assuming that the content of the user's `.cshrc` and `.login` is trivial and does not interfere with the rest of the setup on needs to run the following to initialize the PHENIX computing environment:
```
/opt/phenix/core/bin/phenix_setup.csh -n
```
The parameter -n wipes the existing PHENIX setup. In the PHENIX software environment, the /opt/phenix directory contains 3rd party libraries (like ROOT and GEANT4) needed to develop and run our code. The `phenix_setup.csh` script sets an environment variable OFFLINE_MAIN which points to the installation area for our libraries. 

##### Useful Links
{% include navigation/findlink.md name='cvs_cheatsheet' tag='CVS "cheat sheet"' %}

##### Archived presentations
[A 2006 introduction to the PHENIX software framework]({{ '/assets/misc/simTutorial02Aug2006.pdf' | relative_url }})


