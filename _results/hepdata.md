---
name: hepdata
layout: newbase
---
{% include layouts/find_title.md name=page.name %}
##### The Policy
{% include_cached navigation/findlink.md name='HEPData' %} is an open-access
repository for scattering data from experimental particle physics. _It includes
data points_ from several thousand publications produced by multiple
Collaborations working in High Energy and Nuclear Physics,
and is hosted by CERN as a part of its Open Data initiative.
The PHENIX Collaboration is using this platform as one of the principal components of its
{% include navigation/pagelink.md folder=site.about name='dap' tag='Data and Analysis Preservation (DAP) effort' %}
and manages a growing
{% include navigation/findlink.md name='PHENIX on HEPData' tag='collection of HEPData entries' -%}.

**By the policy established by the PHENIX IB, every paper containing tables and/or plots must be
accompanied by a HEPData-compliant data package** containing the tables and/or plots data
before it is approved for publication. Please see the official policy document (sec. IV.iv):
{% include_cached documents/doc.md type='document' tag='pub_policy' %}

Specifically:
> "The IRC shall be empowered to adjudicate disagreements on the details of the paper.
> A near-consensus shall be a pre-requisite for the submission of the paper to the
> preprint arXiv and journal, but only after the IRC has certified that data tables are
> available in proper format for later submission to HEP data."

##### The Format
The data package prepared for submission to HEPData must conform to the specific
format required by the HEPData portal -
please see the {% include navigation/findlink.md name='hepdata_submission' tag='HEPData documentation' %}
for details of the requirements. There is a useful
{% include navigation/findlink.md name='hepdata_tips' tag='collection of tips' %}
on the HEPData site, please peruse it. In addition, the DAP team created
{% include navigation/findlink.md name='github_hepdata_examples' tag='a few simple examples' %}
kept in the PHENIX repository on GitHub to illustrate basic features and options of the HEPData format.
Beginners are encouraged to experiment with these examples by using the "sandbox" feature of the
HEPData Portal (see **Appendix B** below).

The basic idea of how a submission is structured is as follows.
Data contents of each item included in the package (e.g. a plot) are described
in a corresponding individual file formatted as YAML (e.g. if there are 5 plots in the paper you are expected to
provide 5 YAML data files). In addition, a special YAML file *submission.yaml* describes the submission as a whole
e.g. provides the names of the data and optional image files, **list of keywords** etc.
It also contains an abstract (typically imported as LaTeX from the publication material);
unfortunately, not every LaTeX feature will work correctly on HEPData and the output will
need to be checked (see the "sandbox" reference below).

Since YAML allows comments - lines starting with a "**#**" sign - it is very easy to add any
sort of extra information to *submission.yaml* that may be helpful for communication with
members of the Collaboration, reviewers and for the workflow of the submission process in general.
For example, it is necessary to provide the **Inspire ID** of the paper
for the HEPData submission. It can be placed in a comment line. Also, 
including the PHENIX-internal **PPG identifier** is highly recommended
as it reduces the chances of human error and facilitates communication.
Both Inspire ID and the PPG identifier can be easily incorporated
in the comment lines of the *submission.yaml* file mentioned above
(i.e. in lines of text starting with "#"). There can be any number of comment lines.
Including information about the designated reviewer (member of the IRC for the paper)
as an additional comment line is encouraged. The following pattern of the top of the *submission.yaml*
file may help illustrate this:
```yaml
# PPG999
# InspireHEP: 99999
# Reviewing IRC member: M.Phenix mphenix@bnl.gov
```
This is not to be confused with the *comment* attribute of the YAML file which almost always contains
the abstract of the published paper, typically typeset in LaTeX:
```yaml
comment: The PHENIX Collaboration at the Relativistic Heavy Ion Collider has measured
open heavy-flavor production in minimum bias Au$+$Au collisions at $\sqrt{s_{NN}}=200$ GeV
```
It is probably the easiest to use existing examples of the *submission.yaml* files for guidance.
They can be found in the {% include navigation/findlink.md name='hepdata_github' tag='official PHENIX repository' %}.


If there are existing data files in an ad-hoc format (text etc) these can be converted
to the HEPData format with some effort. The DAP team is looking at technical
solutions to facilitate this process. For example, if plots are generated
using ROOT macros the code can be instrumented to output same
data in a format compatible with HEPData.
There is a helpful write-up about preparing data for upload:
{% include_cached documents/doc.md type='writeup' tag='nattrass' %}

##### Keywords: an Overview
Like with many other data repositories, consistent use of keywords is essential for
data discoverability. HEPData makes it possible to attach a set of keywords and
keyphrases to the submission package, by adding a properly formatted section to
the *submission.yaml* file as illustrated below:
```yaml
keywords: # used for searching, possibly multiple values for each keyword
- {name: reactions, values: [P P --> Z0 Z0 X]}
- {name: observables, values: [SIG]}
- {name: cmenergies, values: [7000.0]}
- {name: phrases, values: [Inclusive, Integrated Cross Section, Cross Section, Proton-Proton Scattering, Z Production, Z pair Production]}
```				   
<!--   -->
The {% include navigation/findlink.md name='hepdata_keywords' tag='HEPData keywords page' %}
contains useful  details. {% include navigation/findlink.md name='github_hepdata_examples' tag='The examples' %}
created by the PHENIX team as tutorials illustrate how the keywords are placed in the *submission.yaml* file.
The examples use a slightly different YAML notation which is equally valid:
```yaml
keywords:
- name: observables
  values: [MASS]
- name: cmenergies
  values: [2000.0]
- name: reactions
  values: [P P --> GAMMA GAMMA X]
- name: phrases
  values: ['PHENIX', 'ppg999', 'example 1', 'gamma gamma', 'Proton-Proton Scattering']
```
<!-- -->
##### Reactions, Particles and Phrases
In the snippet of YAML code shown above, the "reactions", "cmenergies" and "observables" are
*predefined keywords* while the last item (*phrases*) contains optional key phrases supplied
by the user (which can theoretically contain anything).

If applicable, it is very helpful to include a description of the **reaction(s)**
pertinent to the publication in the keywords section, e.g.
```yaml
# note that contrary to other notation systems there is no "+" sign anywhere
- {name: reactions, values: [P P --> Z0 Z0 X]}
# alternative notation for the same reaction that can be used interchangeably
- name: reactions
  values: [P P --> Z0 Z0 X]
```
<!-- -->
When describing the reactions it is important to use the
{% include navigation/findlink.md name='hepdata_particles' tag='particle notation' %}
universally used on the HEPData portal. Note that 'Au' (the gold nucleus) is conspicuously missing
from the list, but Uranium is included. Since particle names are capitalized as per HEPData
convention it is recommended to use 'AU' whenever a reference to the gold nucleus is needed.
Quarks are denoted as 'UQ', 'DQ' and so on. As seen in the example above, in the decription
of a reactions particles are separated by space, and the arrow is depicted in alphanumeric characters.

The "phrases" section can contain essentially any sort of key phrases including completely new ones,
however it is helpful to start with the
{% include navigation/findlink.md name='hepdata_phrases' tag='list of key phrases' %}
historically used on HEPData since they are more likely to be used in queries on the site.
Note that
{% include navigation/pagelink.md folder=site.results name='keywords' tag='the "keywords" page' %}
on this PHENIX site contains keywords to be used primarily for the PHENIX materials uploaded to the
{% include navigation/pagelink.md folder=site.results name='zenodo' tag='Zenodo' %} portal,
which are mostly distinct from the HEPData
{% include navigation/findlink.md name='hepdata_phrases' tag='conventions' %}.
If you have any comments or suggestions regarding the keywords please contact the
{% include navigation/pagelink.md folder=site.about name='dap_contact' tag='DAP Team' %}.
				   
##### The Procedure
Each collaboration using the HEPData portal has a
{% include navigation/findlink.md name='hepdata_coordinators' tag='coordinator' %}
registered on that Web resource, and that person is reponsible for managing the submission workflow,
making corrections, communicating with reviewers etc. At the time of writing, PHENIX has delegated this
responsibility to M.Potekhin (potekhin_at_bnl_dot_gov).
It is assumed that the PPG members responsible for the HEPData submission have GitHub
accounts since the workflow involves a dedicated section of the 
{% include navigation/findlink.md name='hepdata_github' tag='official PHENIX repository' %}.
**The procedure of publishing materials on HEPData does include a few steps but still is fairly straighforward.**
It relies on 
1. having properly formatted data
2. designating a reviewer - member of the IRC
3. making use of GitHub to keep and manage the material and make corrections if necessary

Here are the details of the procedure:
* The IRC is responsible for QA of the data. The IRC selects one of its members as the official
reviewer of the data uploaded to the HEPData portal who checks the data and gives their final approval
before data goes live.  **Important: the reviewer needs to create a regular account on the HEPData portal
with their regular e-mail address so that notifications be can properly
forwarded.** Getting registered as a user is very much straightforward.
* The submission package for a given publication is prepared by the working group in the form
of properly formatted YAML (and optional PNG) files.
The HEPData portal provides adequate documentation on this and other subjects.
* There is a mandatory *submission.yaml* file describing the package. It is strongly recommended
that the comments included in this file *(lines starting with '#')* include the **Inspire ID**
of the publication, the **internal PPG ID** and the name and e-mail address of the designated IRC
member for final approval. This is not to be confused with the *"comments"* tag which traditionally
contains the abstract of the publication as it was published.
* Validation step:
   * Optional: please see **Appendix A** for a simple way to confirm basic validity of the format
of your submission.
   * Strongly recommended: use the **sandbox** feature on the HEPData Portal (see **Appendix B**). Since
HEPData pages are content-rich it is easy to overlook errors both in typesetting and in consistency
of the numerical data. Using the sandbox and carefully examining the rendered page is extremely
helpful in reducing errors which may result in having to resubmit the whole package.
* After validation, the submission package (i.e. a collection of files created for HEPData)
is added to a specific folder of the PHENIX repository on GitHub (please see **Appendix C** below).
If you created **".gz" or a ".tar" files** for testing purposes, please
make sure these are not checked into the git repository, it is not necessary and may create ambiguity
regarding the primary source of the data. Just remove such files when you are ready to commit to the repo
and only keep YAML and optional image files.
* Once notified, **the DAP team will upload the package to HEPData** and perform basic checks.
* If all looks good, the designated IRC member will be notified that they need to review the
uploaded data. This is done via a Web link.
* *Each table or plot is approved separately by the designated IRC member.* If errors are found,
corrections should be made and checked into the repository (Appendix C), and a pull request created,
effectively repeating the cycle. The PHENIX HEPData coordinator will then update the material on
the site and notify the reviewer.
* After each item in the submission is approved the PHENIX HEPData coordinator
will finalize the submission. At this point, it becomes globally visible on the HEPData portal
and the process is complete.

Please contact the {% include navigation/pagelink.md folder=site.about name='dap_contact' tag='DAP Team' %} for
more information.

##### Pitfalls
* Incorrect or missing keywords/key phrases
* Garbled, incorrect or suboptimally formatted content of the abstract due to errors
made while copying the abstract from other sites or documents and limitations of the
HEPData LaTeX implementation
* Incorrect notation used for reactions e.g. "p+p" as opposed to "[P P --> X]"
* Leftover .tar, .gz or .tgz files accidentally checked into the repository
* Missing image files with only the thumbnail images provided. Images are optional but
if this option is selected it must be done right
* Mismatch between the data and the provided optional image

##### Correcting Errors
It is strongly recommended to pay close attention to the content of your submission i.e.
numerical values of the the data points, error bars, labels and scales of axes etc, such
that the submission is final and would never need any adjustments.
If, despite best effort, there is an inaccuracy in a submission it can be corrected. This
requires that the complete package be resubmitted by the HEPData coordinator for PHENIX.
In that case, a **new version** of the HEPData entry is created on the portal and becomes
available by default under the same HEPData ID, while the old version is still available
via the specific reference ("v1" etc).
While this guarantees that the data presented on the site is the most accurate according to our
judgement it also creates certain ambiguity for people who already accessed the old data and
perhaps performed a few downloads. While this can addressed by communicating the fact of
the correction, such situations should be avoided so the quality of the original submission is
paramount.


{{ site.hr }}
##### Appendix A: YAML validation (offline)

The Python package "hepdata-validator"
({% include navigation/findlink.md name='hepdata_validator' tag='available from GitHub' %})
can be used to quickly check validity of a file. You may need to use a standard Python utility
like *pip* or its equivalent to install this package. A simple example of usage:
				   
```python
>>> from hepdata_validator.data_file_validator import DataFileValidator
>>> df=DataFileValidator()
>>> df.validate(file_path='myGoodFile.yaml')
True
>>> df.validate(file_path='myBadFile.yaml')
False
```

##### Appendix B: The Sandbox
The "sandbox" feature of the HEPData portal allows the user to thoroughly validate the
submission package. It will catch trivial errors in YAML formatting, typos in the provided
filenames, missing files etc. Importantly, it helps to determine
whether the LaTeX-formatted abstract is rendered correctly - 
it is hard to guarantee that the LaTeX dialect used on the HEPData
site will produce adequate output.

Using the sandbox feature requires an account on HEPData
which is **trivial to obtain**. Once you log into the portal, the "sandbox" option will be
clearly marked in the menu in the upper right corner of the Web page.
The sandbox won't be visible to anyone without the link generated by the system, so the data
are protected in this manner. Uploading material will require creation of a *tar* archive of your
files. You may want to delete the tar file once you complete validation to keep the repository
folder clean.

The sandbox section has a useful "dashboard" feature which allows the user to keep track of
their test submissions. You can delete the entries you no longer need from your sandbox to
make navigation easier.

If an upload to the sandbox is successful, the Web page will eventually refresh and the
rendered contents will be shown. Time required to render the contents of your submission
will depend on its complexity - simple single-table submissions will render in 10-20 sec
while complex multi-table entries may take minutes. If there is a failure, the user is redirected to the file upload
page. Either way, there is a notification sent via e-mail telling the user about the
status of their submission (i.e. success or failure). Diagnostic messages generated
by the sandbox validation system and delivered via e-mail are often quite useful
and help to identify problems quickly.
				   
##### Appendix C: the GitHub Workflow
The HEPData materials are kept in a designated folder in the 
{% include navigation/findlink.md name='hepdata_github' tag='PHENIX Collaboration HEPData repository on GitHub' %}.
Adding your HEPData files to the repository is done as follows:
* Create a fork of the repository on GitHub (easy to do in the Web UI).
* Clone the resulting repository to your workstation/laptop.
Look at the existing 'ppg' folders under assets/hepdata if you need examples.
* Check if the correct "*ppgXYZ*" folder for your submission exists, if not create it and "git add" it to your repository. 'XYZ' here stands for the 3-digit PPG serial number i.e. if you are in PPG 433 you will need to create a folder "ppg433". For PPG 71 that would be "ppg071".
* Populate the folder with your HEPData submission files.
* Create a *tar* file with the contents of the folder and peruse the **sandbox** functionality of HEPData as suggested above
to upload and validate the contents.
* If you are satisfied with the submission and there are no errors, delete the ".tar" or ".gz" file(s) and
do a "git commit ." and "git push" to place the material in your fork on GitHub (do not push to "master").
* Create a pull request on the GitHub website in order to merge your addition into the repository. The DAP team will take care of the rest.


