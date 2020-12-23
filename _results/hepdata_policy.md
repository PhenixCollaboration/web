---
name: hepdata_policy
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

Detailed information for preparing and uploading HEPData materials can be found on the 
{% include navigation/pagelink.md folder=site.results name='hepdata_instructions' tag='HEPData instructions page' %}.
