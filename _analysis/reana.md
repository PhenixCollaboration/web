---
name: reana
layout: newbase
---
{% include layouts/find_title.md name=page.name %}

This page is work in progress.

{% include navigation/findlink.md name='reana' tag='REANA' %} is a reproducible research data analysis platform developed at CERN.
It is considered for Analysis Preservation in PHENIX due to the following features:

* Unambiguous description of workflows (encoded in a YAML schema)
* Capture and preservation of both the software and the software environment by using containerization

Execution of workflows in REANA requires a properly configured *REANA cluster*. One such cluster is available to CERN users. There is also a test instance currently beinf evaluated at BNL (on the internal network only).
