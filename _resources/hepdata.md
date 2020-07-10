---
name: hepdata
layout: newbase
---
{% capture dap_page_url %}{% include navigation/findpage.md folder=site.about name='dap' %}{% endcapture %}
{% capture kw_url %}{% include navigation/findpage.md folder=site.resources name='keywords' %}{% endcapture %}
{% capture team_url %}{% include navigation/findpage.md folder=site.about name='contact' %}{% endcapture %}

{% include layouts/find_title.md name=page.name %}

{% include navigation/findlink.md name='HEPData' %} is an open-access repository for
scattering data from experimental particle physics which includes data points from several thousand publications.

The PHENIX Collaboration is using this platform as one of the components of its
[Data and Analysis Preservation (DAP) effort]({{ dap_page_url }}), and is adding material to
its {% include navigation/findlink.md name='PHENIX on HEPData' title='collection of HEPData entries' -%}.
Members of the PHENIX Collaboration interested in creating materials suitable for submission to HEPData
are encouraged to contact the [DAP Team]({{ team_url }}).
