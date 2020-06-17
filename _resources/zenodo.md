---
name: zenodo
layout: newbase
---
{% capture dap_page_url %}{% include navigation/findpage.md folder=site.about name='dap' %}{% endcapture %}
{% capture kw_url %}{% include navigation/findpage.md folder=site.resources name='keywords' %}{% endcapture %}
{% capture team_url %}{% include navigation/findpage.md folder=site.about name='contact' %}{% endcapture %}

{% include layouts/find_title.md name=page.name %}

[Zenodo](https://about.zenodo.org/){:target="_blank"} is an Open Science Digital Repository launched at CERN in 2013. Its operation is governed by a set of [defined principles](https://about.zenodo.org/principles/). It features a rich set of [search capabilities](https://help.zenodo.org/guides/search/){:target="_blank"} and is backed up by a [robust infrastructure](https://about.zenodo.org/infrastructure/){:target="_blank"}.

The PHENIX Collaboration has elected to use this platform as one of the principal components of its <a href="{{ dap_page_url }}">Data and Analysis Preservation (DAP) effort</a>. Zenodo supports the concept of the "community" whereby documents submitted for archival are curated and become a part of the community collection. Correspondingly, the {% include navigation/phenix_zenodo_collection.md %} has been created and is actively managed, with new uploads being routinely added.

The <a href="{{ team_url }}">PHENIX DAP team</a> maintains <a href="{{ kw_url }}">a list of keywords</a> assigned to materials uploaded by Zenodo in order to facilitate queries.

