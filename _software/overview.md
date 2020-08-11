---
name: software_overview
layout: newbase
---
{% capture build_page_url %}{% include navigation/findpage.md folder=site.software name='build_tools' %}{% endcapture %}

{% include layouts/find_title.md name=page.name %}

The PHENIX software history and its evolution covers approximately 30 years.
Two frameworks form its foundation:
* PISA: simulation framework based on Geant 3
* fun4all: reconstruction and analysis framework. Motivated by neccessity of integrating of code developed independently for many subsystems and bring it under one umbrella

Many components of the software (e.g. analysis) rely on a set of [build tools]({{ build_page_url }})
which include 
{% include navigation/findlink.md name='automake' -%},
{% include navigation/findlink.md name='autoconf' -%},
{% include navigation/findlink.md name='libtool' -%}.

#### Archived presentations
[A 2006 introduction to the PHENIX software framework]({{ '/assets/misc/simTutorial02Aug2006.pdf' | relative_url }})


