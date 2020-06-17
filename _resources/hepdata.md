---
name: hepdata
layout: newbase
---
{% capture dap_page_url %}{% include navigation/findpage.md folder=site.about name='dap' %}{% endcapture %}
{% capture kw_url %}{% include navigation/findpage.md folder=site.resources name='keywords' %}{% endcapture %}
{% capture team_url %}{% include navigation/findpage.md folder=site.about name='contact' %}{% endcapture %}

{% include layouts/find_title.md name=page.name %}

[HEPData](https://www.hepdata.net/){:target="_blank"} is an open-access repository for scattering data from experimental particle physics which includes data point from several thousand publications.

The PHENIX Collaboration has started using this platform as one of the components of its <a href="{{ dap_page_url }}">Data and Analysis Preservation (DAP) effort</a>. It is adding to its [collection of HEPData entries](https://www.hepdata.net/search/?q=phenix){:target="_blank"}.
