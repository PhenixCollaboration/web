---
name: hepdata
layout: newbase
---
{% include layouts/find_title.md name=page.name %}

##### About
{% include_cached navigation/findlink.md name='HEPData' %} is an open-access repository for
scattering data from experimental particle physics which includes data points from several thousand publications.
The PHENIX Collaboration is using this platform as one of the components of its
{% include navigation/pagelink.md folder=site.about name='dap' tag='Data and Analysis Preservation (DAP) effort' %}, and is adding material to
its {% include navigation/findlink.md name='PHENIX on HEPData' tag='collection of HEPData entries' -%}.
Members of the PHENIX Collaboration interested in creating materials suitable for submission to HEPData
are encouraged to contact the {% include navigation/pagelink.md folder=site.about name='contact' tag='DAP Team' %}.

##### The Procedure
In order for data to be successfully uploaded to the HEPData portal, it must conform to a specific format (please check the HEPData site for documentation). Existing text files can be converted to the HEPData format with some effort. There is a helpful write-up about preparing data for upload:
{% include_cached documents/doc.md type='writeup' tag='nattrass' %}

Currently the following procedure is suggested:
* The submission package for a given publication is prepared in the form of properly formatted YAML (and optinal PNG) files.
* There is a sandbox feature on HEPData which allows to validate the submission package and in particular whether the LaTeX-formatted abstract is rendered correctly. Please use it.
* We use *git* for version control and GitHub for development, sharing and keeping custodial copies of the material. The submission package should be added to a specific folder on GitHub: [https://github.com/PhenixCollaboration/documentation/tree/master/assets/hepdata](https://github.com/PhenixCollaboration/documentation/tree/master/assets/hepdata){:target="_blank"}. This is done as follows:
   * Create a fork of the "documentation" repository on GitHub (easy to do in the Web UI)
   * Clone the resulting repository
   * Check if the correct "ppgXXX" folder exists, if not create it and add it to your repository. 'XXX' stands for the PPG serial number; populate the folder with your HEPData submission files
   * Do "git commit ." and "git push" to place the material on GitHub
   * Create a pull request on the GitHub website so that the {% include navigation/pagelink.md folder=site.about name='contact' tag='DAP Team' %} can merge your addition into the official repository

The DAP team will then take care of the actual upload to HEPData and related procedures. You will be notified when this process completes which shouldn't take long.

{% include_cached documents/doc.md category='hepdata' type='publication' title="Uploaded HEPData materials" -%}
