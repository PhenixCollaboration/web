---
name: hepdata_policy
layout: newbase
---
{% include layouts/find_title.md name=page.name %}
##### The Policy
{% include_cached navigation/findlink.md name='HEPData' %} is an open-access
repository for scattering data from experimental particle physics. It stores and
provides access to
data points from several thousand publications produced by multiple
Collaborations working in High Energy and Nuclear Physics, and is hosted by
CERN as a part of its Open Data initiative. It is a durable and well-supported
platform. The PHENIX Collaboration is using HEPData as one of the principal
components of its
{% include navigation/pagelink.md folder=site.about name='dap' tag='Data and Analysis Preservation (DAP) effort' %}
and manages a growing
{% include navigation/findlink.md name='PHENIX on HEPData' tag='collection of HEPData entries' -%}.
Each entry is a specially formatted data package representing numerical data used in figures and tables in a particular publication. The HEPData portal has the functionality to produce nicely
formatted web pages complete with data tabulation, plot visualization etc.
Only publications which are indexed on the
{% include_cached navigation/findlink.md name='Inspire' tag='InspireHEP' %} portal are eligible for
this process.

**By the policy established by the PHENIX IB, every paper containing tables and/or plots must be
accompanied by a HEPData-compliant data package** containing the tables and/or plots data
before it is approved for publication. Please see the official policy document (sec. IV.iv):
{% include_cached documents/doc.md type='document' tag='pub_policy' %}

Specifically:
> "The IRC shall be empowered to adjudicate disagreements on the details of the paper.
> A near-consensus shall be a pre-requisite for the submission of the paper to the
> preprint arXiv and journal, but only after the IRC has certified that data tables are
> available in proper format for later submission to HEP data."

Detailed information for preparing and uploading HEPData materials can be found on the 
{% include navigation/pagelink.md folder=site.results name='hepdata_instructions' tag='HEPData instructions page' %}.

##### Outline of the Procedure
Each collaboration using the HEPData portal has a
{% include navigation/findlink.md name='hepdata_coordinators' tag='coordinator' %}
registered on that Web resource. That person is reponsible for managing the submission workflow,
such as initiating the submission and communicating with PPG and IRC, as well as handling exceptional
situations such as modifications to the published HEPData entries. At the time of writing, PHENIX
has delegated this responsibility to M.Potekhin (potekhin_at_bnl_dot_gov).

It is assumed that the PPG members responsible for the HEPData submission have GitHub
accounts and basic GitHub proficiency since the workflow involves a dedicated
{% include navigation/findlink.md name='hepdata_github' tag='PHENIX repository' %}.

The procedure of publishing materials on HEPData includes the following principal elements:
1. Having a properly formatted data package and making use of GitHub to manage prepared materials (e.g. to make corrections if necessary).
2. Designating an **uploader** - member of the PPG. This person will perform the file upload and be reponsible to making additions and corrections if necessary.
3. Designating a **reviewer** - member of the IRC. This person will the submitted material and will either approve it, or direct corrections requests to the uploader.
4. Notifying the HEPData Coordinator so that the process can be initiated.

The central part of the publishing process is the review of the submission package.
This involves communication between the reviewer and the uploader
(for example, a request to fix some erroneous data or a typo). This is done optimally by using
a messaging system built into the HEPData portal and accessible directly from the web page created for each submission.
For this reason, it is expected that both the uploader and the reviewer have regular accounts on the HEPData portal.
If this is not already the case, getting registered is straightforward. The e-mail addresses used for
registration need to be communicated to the PHENIX HEPData coordinator (see above) to properly
initiate the submission process. Optionally, this information may be included as '#' comments
into the *submission.yaml* file (see {% include navigation/pagelink.md folder=site.results name='hepdata_instructions' tag='the instructions' -%}).

The following diagram illustrates the flow of communication among the three principal participants of the
HEPData process: the coordinator, the uploader and the reviewer.

{% include images/image.md name='hepdata_workflow' width=669 %}
