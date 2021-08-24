---
name: links
layout: newbase
items:
   - 'PHENIX on Inspire'
   - 'PHENIX on HEPData'
   - 'PHENIX Community on Zenodo'
   - 'PHENIX Collaboration on GitHub'
---
{% include layouts/find_title.md name=page.name %}

{% for item in page.items %}
{%- include navigation/findlink.md name=item category='general' %}
{% endfor %}

##### Legacy Materials
Starting in 2019 the PHENIX Collaboration is relying on the HEPData portal to preserve data content
of its publications (figures and tables). Previously such data was available in *ad hoc* formats
on the legacy website. We are currently migrating a subset of these materials to this web resource.
Please see
[this page]({{ "results/legacy.html" | relative_url }}) for links.

Please notify the 
{% include navigation/pagelink.md folder=site.about name='dap_contact' tag='Data and Analysis Preservation team' %}
should you encounter the 404 page such as [this one]({{ "404.html" | relative_url }}).
