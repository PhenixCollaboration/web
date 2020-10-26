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

##### Legacy Links
The legacy website of the PHENIX Collaboration contained the "papers" page which served both as a catalog of its
publications and a collection of links to the publication-related data tables. Please see
[this page]({{ "papers.html" | relative_url }}) for details.
Please notify the 
{% include navigation/pagelink.md folder=site.about name='dap_contact' tag='Data and Analysis Preservation team' %}
should you encounter the 404 page such as [this one]({{ "404.html" | relative_url }}).
