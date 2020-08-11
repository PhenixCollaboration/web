---
name: embeddingVtx
layout: newbase
---
{% capture build_page_url %}{% include navigation/findpage.md folder=site.software name='build_tools' %}{% endcapture %}
{% capture pisa_page_url %}{% include navigation/findpage.md folder=site.software name='pisa' %}{% endcapture %}

#### About
This page is work in progress and is designed to capture the details of the VTX analysis first performed by Takashi Hachiya.
A repository has been created on GitHub in order to control the code changes - not as a replacement
for CVS but as a temporary holding area:
```
https://github.com/buddhasystem/phenix/tree/master/embed
```
Please consult the [build tools page]({{ build_page_url }}) if you need more information and context for
Autogen.sh, configure.ac, Makefile.am etc

#### Install
The install process:
```
source /opt/phenix/bin/phenix_setup.csh -n new
CVSROOT=/afs/rhic/phenix/PHENIX_CVS/
make distclean
# Please set the "MYINSTALL" variable here, like in the Wiki link above...
/direct/phenix+u/mxmp/software/offline/analysis/dstmerge/autogen.sh --prefix=$MYINSTALL
make
make install
```
Slight variations of the above chain of commands tend to lead to some "libtool" error, this needs to be looked at.

#### VTX Embedding
##### The Improved Setup

Example layout of the "embed" folder (referred to in the variable $EMBEDDING_HOME which is set in the setup script)
```
drwxr-sr-x 3 mxmp rhphenix 4096 Jul 31 16:31 embed
drwxr-sr-x 3 mxmp rhphenix 4096 Jul 31 10:43 real
drwxr-sr-x 2 mxmp rhphenix 4096 Aug  5 20:57 setup
drwxr-sr-x 5 mxmp rhphenix 4096 Jul 30 19:59 sim
```
The "setup" folder is a new one (i.e. not present in the original code base and added for this study).

Embedding is a process with many moving parts and data elements. In order to facilitate this process, we have established
an interim convention to try and keep things as transparent as possible:
* the location of all scripts and supporting files is relative to the directory defined as $EMBEDDING_HOME 
* there is a setup script in the "setup" directory as seen above, which defines
   * **$EMBEDDING_HOME** - root of the directory tree containing all necessary code
   * the **$DATADIR** - which contains ALL data pertinent to a particular embedding run
   * **$MYINSTALL** - the location of the "lib" directory which contains ALL shared libraries

#### Run the single particle simulation
Takashi's working directory used as a starting point:
```
/gpfs/mnt/gpfs02/phenix/hhj/hhj1/hachiya/15.08/embed/sim
```
Under this directory, see the following 3 directories
* gen (single particle generation by the simple random number generator)sim/gen/phparticlegen_pip.csh
* pisa (GEANT3)  sim/pisa/submit/pisa_phpythia.csh
* reco (making DST using the GEANT output)   reco/submit/pisaToDST.csh
Their use is explained in the following sections

#### Single Particle
The script '''phparticlegen_pip_updated.csh''' serves to invoke ROOT:
```
root -b -q  'phparticlegen_pip.C(N, '$pid', "'"$outname"'")'
```
It has two input arguments at this point
* Number of events to be generated
* sequence number (so one can have multiple files)

#### PISA
Current version of the script:
```
pisa/submit/pisa/pisa_phpythia_updated.csh
```
Takes three arguments
* Job number (seq)
* Number of events
* Path to the input file

#### PISA to DST
Current version of the script:
```
reco/submit/pisaToDST_updated.csh
```
Takes three arguments:
* Job number (seq)
* Number of events
* Input file

#### Make the data DST with raw detector hits
Takashi's working directory used as a starting point:
```
/gpfs/mnt/gpfs02/phenix/hhj/hhj1/hachiya/15.08/embed/real
```

The current version can be located under $EMBEDDING_HOME and is available on GitHub at the link above.

$EMBEDDING_HOME/dstmerge/wrk/submit/reco_rawhit_updated.csh is a script to run the reconstruction and save the raw hit in DST.
Zvertex position is also limited with a certain range in the script to match the Z-vertex position  between real and simulation.

The reconstruction macro (Fun4All_CA_merge.C) creates number of files which contain the reconstructed events for the specific trigger.
One can see the trigger labels in the filename like MB (Minimum bias), ERT (EMCal-RICH Trigger), MU(Muon trigger), UP(Ultra-peripheral), OT(others).
Example:
```
CNTmerge_ERT-0000409151-0018.root
CNTmerge_MB-0000409151-0018.root
CNTmerge_MU-0000409151-0018.root
CNTmerge_OT-0000409151-0018.root
CNTmerge_UP-0000409151-0018.root
```

Which file is good for the embedding step  depends on what the user want to do.
The MB file is often used to mix an MB event and a single particle simualation for the efficiency study.

The next step is to run run_embed_updated.csh to mix the real data and simulation (see next section)

#### Embedding
Starting point:
```
/gpfs/mnt/gpfs02/phenix/hhj/hhj1/hachiya/15.08/embed/embed
```

Current location of the script $EMBEDDING_HOME/embed/submit/run_embed_updated.csh.
It is meant to merge the raw hit in real data and simulation, and to run the reconstruction using the merged hits.
```
run_embed_updated.csh <job_number> <event number> <input real DST> <input SIM DST> <output DST> <output ntuple> <output ntuple2>
```

Dependency: svx_cent_ana

#### Event Display
```
/gpfs/mnt/gpfs02/phenix/hhj/hhj1/hachiya/15.08/source/svx_cent_ana
```

* svx_cent_ana/wrk/embeddisp.cc is a tool to see the detector hits from real, sim, and  embed data simultaneously. This is used to make the display shown in p.9 of the slide above.


