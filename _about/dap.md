---
layout: newbase
name: dap
---
{% include layouts/find_title.md name=page.name %}

##### What is DAP?
Since the second decade of the 21<sup>st</sup> century the term **Data and Analysis Preservation** (DAP)
is often used in place of the traditional "data preservation" to account for
the fact that data which can’t be analyzed is useless. DAP is commonly described as a union of
* **Bit preservation** (e.g. data on tape and relevant management policies and techniques). PHENIX relies on capabilities and infrastructure the Scientific Data and Computing Center (SDCC) at Brookhaven National Laboratory for the long-term preservation of the experiment's data
including the raw data, conditions-type data, simulated and processed data.
* Long-term **management and preservation of the software infrastructure and application code**. PHENIX is using version control (CVS and git) to manage its code, and virtual machine (VM) technology to manage the software configuration.
* **Analysis know-how** (knowledge management). The Collaboration has undertaken an effort to review, curate, systematize and preserve knowledge necessary for the analysis of the data. Creation, development and maintenance of this website is a part of this effort.

##### This Site
This website has been created with the goal to support the DAP mandate of the PHENIX Collaboration,
and more specifically to aid the **Knolwedge Management** aspect of it. Content from multiple
legacy PHENIX and RHIC Web sites and various other information resources is being curated,
systematized and included here in a way that is helpful to the present and future researchers
performing or revisiting analyses of the PHENIX data. **The site is not a substitute for the PHENIX Wiki**
or any other comparable content management system used to keep information which is subject to frequent
changes or ad hoc web pages used as scratch space. The content hosted here is meant to be viable in
the long term. For that reasons, the following considerations were taken into account regarding this site:
* ease of maintenance
* security
* performance
* portability

In order to meet these criteria this website relies on modern static website generator technology
with the following features:
* separation of content (including text as well as numeric data and graphics) from the layout of
individual pages as well as of the website as whole
* management of potentially complex structured data without reliance on databases, by keeping data in JSON, YAML and CSV formats
* use of a highly readable and an easy-to-edit syntax for content creation (the so-called *Markdown* syntax)

To this end, the popular <a href="http://jekyllrb.com/">Jekyll</a> website generator is used, with
additional tools (Javascript libraries and advanced stylesheets) for optimal user experience.

##### Other technologies
* {% include navigation/pagelink.md folder=site.resources name='zenodo' tag='Zenodo'-%}, an open science digital repository at CERN.
* {% include navigation/pagelink.md folder=site.results name='hepdata' tag='HEPData' -%}, a CERN-based repository for publication-related data.
* {% include navigation/pagelink.md folder=site.resources name='rivet' tag='Rivet' -%}, a toolkit for validation of MC generators and code preservation.
* {% include navigation/findlink.md name='github' tag='GitHub'-%}: where PHENIX maintains a set of repositories.
* {% include navigation/pagelink.md name='inspire' folder=site.results tag='Inspire' %}: a trusted community hub helping researchers find accurate scholarly information.


##### Credits
Information collected here was provided and curated by the hard-working members of the PHENIX Collaboration
and its leadership. Special thanks to members of the
{% include navigation/findlink.md name='npps' tag='BNL Nuclear and Particle Physics Software Group' %}
for various contributions and technical advice.
Design of this site was inspired by the
{% include navigation/findlink.md name='hsf' tag='HEP Software Foundation website' %}.
We are grateful to the authors and maintainers of the following technologies:
* <a href="https://pages.github.com/">GitHub Pages</a>
* <a href="http://jekyllrb.com/">Jekyll</a>
* <a href="https://shopify.github.io/liquid/">Liquid</a>
* <a href="http://getbootstrap.com/">Bootstrap</a>

