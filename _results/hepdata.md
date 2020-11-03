---
name: hepdata
layout: newbase
---
{% include layouts/find_title.md name=page.name %}

##### The Repository
{% include_cached navigation/findlink.md name='HEPData' %} is an open-access repository for
scattering data from experimental particle physics. _It includes data points_ from several
thousand publications produced by multiple Collaborations working in High Energy and Nuclear Physics,
and is hosted by CERN as a part of its Open Data initiative.
The PHENIX Collaboration is using this platform as one of the principal components of its
{% include navigation/pagelink.md folder=site.about name='dap' tag='Data and Analysis Preservation (DAP) effort' %}
and manages a growing {% include navigation/findlink.md name='PHENIX on HEPData' tag='collection of HEPData entries' -%}.

##### Policy
By the policy established by the PHENIX IB, every paper containing tables and/or plots must be
accompanied by a **data package** containing the tables and/or plots data before it is approved
for publication. Please see the official policy document (sec. IV.iv):
{% include_cached documents/doc.md type='document' tag='pub_policy' %}

##### The Format
The data package prepared for submission to HEPData must
* Conform to the specific format required by the HEPData portal
(please see the {% include navigation/findlink.md name='hepdata_submission' tag='documentation' %})
* Be certified by the IRC for each publication
* Have an Insipre ID associated with it

Data contents of each item included in the package (e.g. a plot) are described
in a corresponding file formatted in YAML (e.g. if there are 5 plots in the paper you are expected to
provide 5 YAML data files). In addition, a special YAML file *submission.yaml* describes the submission as a whole
and contains other information such as the abstract and the list of keywords. Since YAML allows comments -
lines starting with a "#" sign - it is easy to add any sort of extra information to *submission.yaml* that
may be helpful for communication with members of Collaboration, reviewers and for the workflow of the
submission process in general.

For example, it is necessary to provide the **Inspire ID** of the paper
for the HEPDAta submission. It can be placed in a comment line. Also, 
including the PHENIX-internal **PPG identifier** is highly recommended
as it reduces the chances of human error and facilitates communication.
Both Inspire ID and the PPG identifier can be easily incorporated
in the comment lines of the *submission.yaml* file mentioned above
(i.e. in lines of text starting with "#"). There can be any number of comment lines.

If there are existing date files in an ad-hoc format these can be converted
to the HEPData format with some effort. The DAP team is looking at technical
solutions to facilitate this process. For example, if plots are generated
using ROOT macros the code can be instrumeted to output same
data in a format compatible with HEPData.
There is a helpful write-up about preparing data for upload:
{% include_cached documents/doc.md type='writeup' tag='nattrass' %}

##### The Abstract and the Keywords
The abstract should be formatted as LaTeX and it will be rendered
on the HEPData site however not every LaTeX feature will work correctly and this needs to be checked (see the
"sandbox" feature below).

##### The Procedure
It is assumed that the PPG members responsible for the HEPData submission have GitHub
accounts since the workflow involves a dedicated section of the  official PHENIX repository:
* [https://github.com/PhenixCollaboration/documentation/tree/master/assets/hepdata](https://github.com/PhenixCollaboration/documentation/tree/master/assets/hepdata){:target="_blank"}

The procedure of publishing materials on HEPData includes a few steps but is fairly straighforward
and relies on having (a) properly formatted data (b) a designated reviewer in the IRC (c) making
use of GitHub to manage the material and make corrections if necessary. Here are the details:
* The IRC is responsible for QA of the data. The IRC selects one of its members as the official
reviewer of the data uploaded to the HEPData portal who checks the data and gives final approval
before the data goes live.
* The submission package for a given publication is prepared by the working group in the form
of properly formatted YAML (and optional PNG) files.
The HEPData portal provides adequate documentation on this and other subjects.
* There is a mandatory *submission.yaml* file describing the package.
It is strongly recommended that the comments include the **Inspire ID** of the publication,
the **internal PPG ID** and the name and e-mail address of the designated IRC member for final approval;
this can be done using optional comment lines starting with '#'.
* There is a **sandbox** feature on HEPData which allows to validate the submission
package and in particular whether the LaTeX-formatted abstract is rendered correctly.
Please use it, otherwise it's hard to guarantee that the LaTeX dialect used on the HEPData
site will produce adequate output. Using the sandbox feature requires an account on HEPData
which is **trivial to obtain**. Once you log into the portal, the "sandbox" option will be
clearly marked in the menu in the upper right corner of the Web page.
The sandbox won't be visible to anyone without the link generated by the system, so the data
are protected in this manner.
* The submission package (i.e. a collection of files created for HEPData) is then added to a specific
folder of the PHENIX repository on GitHub (please see **Appendix B** below).
* Once notified, **the DAP team will upload the package to HEPData** and inform the designated
IRC member that they need to review the data already uploaded and issue their final approval.
This is done via a Web link.
* Each table or plot is approved separately by the designated IRC member. If errors are found, corrections
should be made and checked into the repository (Appendix B), and a pull request created
* The PHENIX HEPData coordinator will update the material on the site and notify the reviewer
* After each item in the submission is approved the PHENIX HEPData coordinator
will finalize the submission. At this point, it becomes globally visible on the HEPData portal and the process is complete.

Please contact the {% include navigation/pagelink.md folder=site.about name='dap_contact' tag='DAP Team' %} for
more information. Each collaboration using the HEPData portal has a
{% include navigation/findlink.md name='hepdata_coordinators' tag='coordinator' %}
registered on that Web resource, and that person is reponsible for managing the submission workflow,
making corrections, communicating with reviewers etc. At the time of writing, PHENIX has delegated this
responsibility to M.Potekhin (potekhin_at_bnl_dot_gov).


##### Appendix A: YAML validation

The Python module "hepdata-validator" (available from GitHub) can be used to quickly check validity of a file, e.g.

```python
>>> from hepdata_validator.data_file_validator import DataFileValidator
>>> df=DataFileValidator()
>>> df.validate(file_path='myGoodFile.yaml')
True
>>> df.validate(file_path='myBadFile.yaml')
False
```

##### Appendix B: GitHub Workflow
The HEPData materials are kept in a designated folder in the PHENIX Collabotation documentation repository on GitHub:
[https://github.com/PhenixCollaboration/documentation/tree/master/assets/hepdata](https://github.com/PhenixCollaboration/documentation/tree/master/assets/hepdata){:target="_blank"}.
Adding your HEPData files to the repository is done as follows:
* Create a fork of the "documentation" repository on GitHub (easy to do in the Web UI): [https://github.com/PhenixCollaboration/documentation](https://github.com/PhenixCollaboration/documentation){:target="_blank"}
* Clone the resulting repository to your workstation/laptop.
Look at the existing 'ppg' folders under assets/hepdata if you need examples
* Check if the correct "ppgXXX" folder for your submission exists, if not create it and add it to your repository. 'XXX' here stands for the PPG serial number i.e. if you are in PPG 433 you will need to create a folder "ppg433".
* Populate the folder with your HEPData submission files
* Create a *tar* file with the contents of the folder and peruse the **sandbox** functionality of HEPData as suggested above
to upload and validate the contents
* If you are satisfied with the submission and there are no errors,
do a "git commit ." and "git push" to place the material on GitHub (do not push to "master")
* Create a pull request on the GitHub website in order to merge your addition into the repository

