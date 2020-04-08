---
title: This Website
layout: newbase
abbrev: site
weight: 5
level: 0
---
{% include title.md %}

### The Goal
This website has been created with the goal to support the **Data and Analysis Preservation** (DAP)
mandate of the PHENIX Collaboration, and more specifically to aid the **Knolwedge Management** aspect of it.
Content from multiple legacy PHENIX and RHIC Web sites and various other information resources is being curated,
systematized and included here in a way that is helpful to the present and future researchers performing
or revisiting analyses of the PHENIX data.

**The site is not a substitute for the PHENIX Wiki** or any other comparable content management
system used to keep information which is subject to changes or pages used as a scratch pad
to for developing analyses or other topics. The *long-term* knowledge management is the key
in shaping the content hosted here.

### The Platform
The following considerations are important for long-term viability of the site:
* ease of maintenance
* security
* performance
* portability

In order to meet these criteria this website relies on modern static
website generator technology with the following features:
* separation of content (including text as well as numeric data and graphics) from the layout of individual pages as well as of the website as whole
* management of potentially complex structured data without reliance on databases, by keeping data in JSON, YAML and CSV formats
* use of a highly readable and an easy-to-edit syntax for content creation (the so-called *Markdown* syntax)

To this end, the popular <a href="http://jekyllrb.com/">Jekyll</a> website generator is used, with
additional tools (Javascript libraries and advanced stylesheets) for optimal user experience.


### Credits
Information collected here was provided and curated by the hard-working members of the PHENIX Collaboration
and its leadership. Special thanks to members of the <a href="https://npps.bnl.gov/">BNL Nuclear and Particle Physics Software Group</a> for various contributions and technical advice.
Design of this site was inspired by the <a href="http://hepsoftwarefoundation.org/">HEP Software Foundation</a> Web site.
We are grateful to the authors and maintainers of the following technologies: <a href="https://pages.github.com/">GitHub Pages</a>,
 <a href="http://jekyllrb.com/">Jekyll</a>, <a href="https://shopify.github.io/liquid/">Liquid</a>, <a href="http://getbootstrap.com/">Bootstrap</a>.

<iframe src="https://phenixcollaboration.github.io/web/" height="600" width="800">test</iframe>
