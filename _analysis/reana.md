---
name: reana
layout: newbase
---
{% include layouts/find_title.md name=page.name %}

This page is work in progress.

##### REANA
{% include navigation/findlink.md name='reana' tag='REANA' %} is a reproducible research data analysis platform developed at CERN.
It is considered for Analysis Preservation in PHENIX due to the following features:

* Unambiguous description of workflows (encoded in a YAML schema)
* Capture and preservation of both the software and the software environment by using containerization

Execution of workflows in REANA requires a properly configured *REANA cluster*. One such cluster is available to CERN users. There is also a test instance currently beinf evaluated at BNL (on the internal network only).

##### Getting Started
To be able to access a REANA cluster the user must be issued an access token by the administrators. Assuming the user created a SSH tunnel to the REANA cluster at BNL a test session might look like this:
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
