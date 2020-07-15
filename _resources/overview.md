---
name: overview
layout: newbase
---
{% capture dap_page_url %}{% include navigation/findpage.md folder=site.about name='dap' %}{% endcapture %}
{% capture zenodo_page_url %}{% include navigation/findpage.md folder=site.resources name='zenodo' %}{% endcapture %}
{% capture hepdata_page_url %}{% include navigation/findpage.md folder=site.resources name='hepdata' %}{% endcapture %}
{% capture rivet_page_url %}{% include navigation/findpage.md folder=site.resources name='rivet' %}{% endcapture %}
{% capture publications_page_url %}{% include navigation/findpage.md folder=site.resources name='publications' %}{% endcapture %}

{% include layouts/find_title.md name=page.name %}

The PHENIX Collaboration [Data and Analysis Preservation (DAP) effort]({{ dap_page_url }}) is leveraging
the following platforms to achieve its objectives:

* [Zenodo]({{ zenodo_page_url }}) - open science digital repository at CERN
* [HEPData]({{ hepdata_page_url }}) - a CERN-based repository for publication-related data
* [Rivet]({{ rivet_page_url }}) - a toolkit for validation of MC generators and code preservation
* A set of repositories on {% include navigation/findlink.md name='github' tag='GitHub' %}

A comprehensive listcatalog of publications created by the PHENIX Collaboration is kept
in the {% include navigation/findlink.md name='Inspire' tag='Inspire database' %}. 
The records can be easily found by using the
{% include navigation/findlink.md name='PHENIX on Inspire' tag='"collaboration phenix"' %}
query line.
