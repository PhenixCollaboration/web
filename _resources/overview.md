---
name: overview
layout: newbase
---
{% capture dap_page_url %}{% include navigation/findpage.md folder=site.about name='dap' %}{% endcapture %}
{% capture zenodo_page_url %}{% include navigation/findpage.md folder=site.resources name='zenodo' %}{% endcapture %}
{% capture hepdata_page_url %}{% include navigation/findpage.md folder=site.resources name='hepdata' %}{% endcapture %}
{% capture rivet_page_url %}{% include navigation/findpage.md folder=site.resources name='rivet' %}{% endcapture %}

{% include layouts/find_title.md name=page.name %}

The PHENIX Collaboration [Data and Analysis Preservation (DAP) effort]({{ dap_page_url }}) is leveraging a few
existing technologies and platoforms to achieve its objeectives:

* [Zenodo]({{ zenodo_page_url }}) 
* [HEPData]({{ hepdata_page_url }}) 
* [Rivet]({{ rivet_page_url }}) 
