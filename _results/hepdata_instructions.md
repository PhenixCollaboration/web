---
name: hepdata_instructions
layout: newbase
---
{% include layouts/find_title.md name=page.name %}
##### Summary
An outline of the HEPData publishing process can be found on the
{% include navigation/pagelink.md folder=site.results name='hepdata_policy' tag='"Policy and Procedure" page' %}.
It involves uploading a *tar* or *gzip* archive of data files in the HEPData-compliant format (YAML)
and having the uploaded material checked by a designated IRC member directly on the HEPData site.
Communication between the uploader and the reviewer is arranged by the HEPData coordinator.
Once the uploaded material is reviewed and certified by the IRC it will be made public ("finalized") by the
HEPData coordinator.

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

The basic structure of a submission package is as follows.
Data contents of each item included in the package (e.g. a plot) are described
in a corresponding _individual file_ formatted as YAML. For example, if there are 5 plots
in the paper you are expected to provide 5 YAML data files.
In addition, a special YAML file *submission.yaml* describes the submission package as a whole
e.g. provides the names of the data and optional image files, **list of keywords** etc.
It also contains an *abstract* (typically imported as LaTeX from the publication material);
unfortunately, not every LaTeX feature will work correctly on HEPData and the output will
need to be checked (see the "sandbox" reference below). The text of the abstract is contained
in an attribute of the YAML structure which is named "comment" (which may be confusing).

Since YAML allows comments - lines starting with a "**#**" sign - it is very easy to add
any sort of extra information to *submission.yaml* that may be helpful for communication
with members of the Collaboration, reviewers and for the workflow of the submission process
in general. For example, it is necessary to provide the **Inspire ID** of the paper
for the HEPData submission. It should be placed in a comment line. Also, 
including the PHENIX-internal **PPG identifier** is highly recommended
as it reduces the chances of human error and facilitates communication.
Both Inspire ID and the PPG identifier can be easily incorporated
in the comment lines of the *submission.yaml* file mentioned above
(i.e. in lines of text starting with "#"). There can be any number of comment lines.
Including information about the designated reviewer (member of the IRC for the paper)
as an additional comment line is encouraged but not mandatory. Consider the following mock-up
comment lines (which would be found on  the top of the *submission.yaml*):
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

##### Numerical Data
Both fixed point and scientific notation formats for numerical data will be parsed correctly
on the HEPData portal and visualization will reflect the values properly. The following snippet
of YAML will work properly:
```yaml
dependent_variables:
- header: {name: '$d\sigma/dM_{\gamma\gamma}$', units: 'mb/MeV'}
  values:
  - errors:
    - {label: total, symerror: 0.005}
    value: 1.5e-1
  - errors:
    - {label: total, symerror: 0.005}
    value: 0.19
  - errors:
    - {label: total, symerror: 0.006}
    value: 0.16
  - errors:
    - {label: total, symerror: 0.03}
    value: 0.12
  - errors:
    - {label: total, symerror: 0.02}
    value: 0.09

independent_variables:
- header: {name: 'Invariant Mass $M_{\gamma\gamma}$', units: 'GeV'}
  values:
  - {value: 1.4e-1, low: 0.08, high: 1.7e-1}
  - {value: 0.2, low: 0.18,  high: 0.22}
  - {value: 0.3, low: 0.27,  high: 0.33}
  - {value: 0.4, low: 0.35,  high: 0.43}
  - {value: 0.5, low: 0.47,  high: 0.55}
```
There is one caveat though: data tables in the corresponding sections of the
HEPData page will display these data "as is" i.e. without further conversion.
In the example above, the resulting table on the HEPData page will contain
1.5e-1 and 0.19 in adjacent table cells.
The person responsible for an upload package should decide whether it is acceptable
or desirable to mix two different notaitons in tables.

A separate issue is related to how many decimal places should be kept in the
data point themselves vs their associated errors. This is currently being formalized
as a policy, and if in doubt please contact the DAP team.

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
				   
##### Details of the Procedure
* The uploader (PPG member) and the reviewer (IRC member) are designated by mutual agreement
* The submission package for a given publication is prepared by the PPG in the
form of properly formatted YAML (and optional PNG) files. The HEPData portal provides
adequate documentation on this and other subjects. Note that there is a mandatory *submission.yaml* file
describing the package. It is recommended that the comments included in this file
*(lines starting with '#')* include
   * The **InspireHEP ID** of the publication
   * The **internal PPG ID**
   * Optional: the names and e-mail addresses of the uploader (PPG side) and the reviewer (IRC side)
* Next, the validation step:
   * Optional: please see **Appendix A** for a simple way to confirm basic validity of the format
of your submission i.e. that it is valid YAML.
   * **Strongly recommended: use the sandbox feature** on the HEPData Portal (see **Appendix B**). Since
HEPData pages are content-rich it is easy to overlook errors both in typesetting and in consistency
of the numerical data. Uploading to the sandbox and carefully examining the rendered page is extremely helpful!
Please pay close attention to the content of the abstract to ensure proper rendering of the LaTex source.
* After the initial validation as described above, the submission package (i.e. a collection of files created
for HEPData) is added to a specific folder of the PHENIX repository on GitHub (please see **Appendix C** below).
To avoid ambiguity, please **do not add to the repository any ".gz" or a ".tar" files you may have created.**
* At this point the {% include navigation/pagelink.md folder=site.about name='dap_contact' tag='DAP Team' %}
is notified and a placeholder on the HEPData portal is created which is based on the InspireHEP ID.
This results in a link available to both the uploader and the reviewer.
* The uploader uploads the package (as a .tar or '.gz' file). At this point, a complete rendered page becomes
available at the link provided, but it's not public.
* The reviewer is notified and proceeds to examine the content of the page for the particular submission.
Each table or plot must be approved or commmented on separately. Approved items will be highlighted in green.
If errors are found, comments should be entered by the reviewer into the panel on the right-hand side of the
page and the uploader gets individual notifications via e-mail, for each flagged item. If necessary,
corrections should be made by the uploader, the submission package re-uploaded, and the GitHub folder updated.
* When this process is completed (potentially after a few iterations) and there are no further comments,
the PHENIX HEPData coordinator will declare the submission final. At this point, it becomes globally
visible on the HEPData portal. Congratulations!

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
* Mismatch between the data and the provided optional images

##### Correcting Errors in a Finalized Submission
It is strongly recommended to pay close attention to the content of your submission i.e.
numerical values of the the data points, error bars, labels and scales of axes etc, such
that the finalized material is indeed final and would never need any adjustments.

If, despite best effort, there is an inaccuracy in a finalized submission it can still be corrected
by the HEPData coordinator for PHENIX who must personally resubmit the package with the corrections
included. In that case, a **new version** of the HEPData entry is created on the portal and becomes
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
submission package in the exact form it will be eventually published. It will catch trivial
errors in YAML formatting, typos in the provided
filenames, missing files etc. Importantly, it helps to determine
whether the LaTeX-formatted abstract is rendered correctly - 
the LaTeX dialect used on the HEPData site is slightly non-standard e.g. the "%" is rendered
correctly without a backslash and vice versa, it is impossible to include LaTeX comments in the
abstract body.

Using the sandbox feature requires an account on HEPData
which is quite **trivial to obtain**. Once you log into the portal, the "sandbox" option will be
clearly marked in the menu in the upper right corner of the Web page.
The sandbox won't be visible to anyone without the link generated by the system, so the data
are protected in this manner. Uploading material will require creation of a *tar* archive of your
files. It is a good idea to delete the *tar* file once you complete validation to keep the repository
folder clean. The sandbox section has a useful "dashboard" feature which allows the user to keep track of
their test submissions. You can delete the entries you no longer need from your sandbox to
make navigation easier.

If an upload to the sandbox is successful, the Web page will eventually refresh and the
rendered contents will be shown. Time required to render the contents of your submission
will depend on its complexity - simple single-table submissions will render in 10-20 sec
while complex multi-table entries may take minutes. If there is a failure, the user is redirected to the file upload
page. Either way, there is a notification sent via e-mail telling the user about the
status of their submission (i.e. success or failure). Diagnostic messages generated
by the sandbox validation system and delivered via e-mail are often useful
and help identify problems.
				   
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
* Create a *pull request* on the GitHub website in order to merge your addition into the repository. The DAP team will
take care of the rest.


