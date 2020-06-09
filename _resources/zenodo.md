---
name: zenodo
layout: newbase
---
{% assign find_dap=site.about | where: "name", 'dap' | first %}
{% assign dap_page_url=find_dap.url  | relative_url %}

{% assign find_kw=site.resources | where: "name", 'keywords' | first %}
{% assign kw_url=find_kw.url  | relative_url %}

{% assign find_team=site.about | where: "name", 'contact' | first %}
{% assign team_url=find_team.url  | relative_url %}

{% include layouts/find_title.md name=page.name %}

[Zenodo](https://about.zenodo.org/){:target="_blank"} is an Open Science Digital Repository launched at CERN in 2013. Its operation is governed by a set of [defined principles](https://about.zenodo.org/principles/). It features a rich set of [search capabilities](https://help.zenodo.org/guides/search/){:target="_blank"} and is backed up by a [robust infrastructure](https://about.zenodo.org/infrastructure/){:target="_blank"}.

The PHENIX Collaboration has elected to use this platform as one of the principal components of its <a href="{{ dap_page_url }}">Data and Analysis Preservation (DAP) effort</a>. Zenodo supports the concept of the "community" whereby documents submitted for archival are curated and become a part of the community collection. Correspondingly, the [PHENIX Community on Zenodo](https://zenodo.org/communities/phenixcollaboration/){:target="_blank"} has been created and is actively managed, with new uploads being routinely added.

The <a href="{{ team_url }}">PHENIX DAP team</a> maintains <a href="{{ kw_url }}">a list of keywords</a> assigned to materials uploaded by Zenodo in order to facilitate queries.

