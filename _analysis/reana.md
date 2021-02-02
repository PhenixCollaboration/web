---
name: reana
layout: newbase
---
{% include layouts/find_title.md name=page.name %}

This page is work in progress.

##### Overview
{% include navigation/findlink.md name='reana' tag='REANA' %} is a reproducible research data analysis platform developed at CERN.
It is considered for Analysis Preservation in PHENIX due to the following features:

* Unambiguous description of workflows (encoded in a YAML schema)
* Capture and preservation of both the software and the software environment by using **containerization**

REANA workflows can be represented as *Directed Acyclic Graphs* which is reflected in the YAML schema based on the 
{% include navigation/findlink.md name='cwl' tag='Common Workflow Language (CWL)' -%}. Each computational component
of a workflow may require a separate and distinct
{% include navigation/pagelink.md folder=site.analysis name='docker' tag='Docker container' -%}.

Execution of workflows in REANA requires a properly configured *REANA cluster*.
One such cluster is available to CERN users, and there are instances at other institutions.
There is also a test instance currently being evaluated at BNL and it is available on the internal BNL network only.
Access to REANA clusters is controlled by granting access tokens to qualified users.

##### Getting Started
To be able to access a REANA cluster the user must be issued an access token by the administrators
(this may be specific to each institution REANA is hosted and typically involves visiting the requisite Web page).

A SSH tunnel is required to access the REANA cluster at BNL. Assuming a token has been obtained
a test session might look like this:
```bash
# create new virtual environment
virtualenv ~/.virtualenvs/reana
source ~/.virtualenvs/reana/bin/activate
# install reana-client
pip install reana-client
# set REANA environment variables for the client
export REANA_SERVER_URL=https://localhost:30443
export REANA_ACCESS_TOKEN=________ # user's REANA token
# clone and run a simple analysis example
git clone https://github.com/reanahub/reana-demo-root6-roofit
cd reana-demo-root6-roofit
reana-client run -w root6-roofit
```
The outputs of REANA workflows (including the example above) are available
for download both via the GUI (the Web pages associated with a given cluster)
and the CLI client.
