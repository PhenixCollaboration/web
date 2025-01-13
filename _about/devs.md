---
layout: newbase
name: devs
---
{% include layouts/find_title.md name=page.name %}
<p/>
<hr/>
##### HEPData
For information about the HEPData process please see the respective
{% include navigation/pagelink.md folder=site.results name='hepdata_policy' tag='policy page' %}.
Items currently in the HEPData pipeline are recorded in a "scratchpad" which is a
{% include navigation/findlink.md name='hepdata_current_spreadsheet' tag='Google Docs Spreadsheet' %} which is subject to frequent changes.


##### Conference keywords and related materials

Conferences appear on two separate pages of this website:
* {% include navigation/pagelink.md folder=site.results name='keywords' tag='"Keywords"' %}
* {% include navigation/pagelink.md folder=site.results name='conferences' tag='"Conferences"' %}

There pages contain renedring of two YAML files in the `_data` folder:
* keywords.yaml -- this is the general registry of the keywords, including those related to conferences
* conferences.yaml -- conference-specific info, such as the URL of the conference web page

Both files are essentially dictionaries and it is important to remember that they share primary keys i.e.
a conference is assigned the same keyword (usually abbreviation like "__hp24__") in both files. In addition to being
an aid in renfering the conference info in tables, in a consistent manner, this keyword is also assigned
to the materials related to the same conference and committed to Zenodo. This is how automated searches work
on these pages, i.e. clicking on a link results in an automated query on the Zenodo portal. The overall consistency
of the keywords is therefore essential for the correct operation of the website.

The formats of both files are quite simple and self-explanatory, so it shouldn't be hard to add materials
just looking at the exeisting patterns.

To be able to group conference listing by the year, on the {% include navigation/pagelink.md folder=site.results name='conferences' tag='"conferences"' %}
page, the source code of this page located in `_results/conferences.md` contains a list of years, on the very top of the file. It is therefore necessary to add
years as necessary, once there are conferences for the new year.


<hr/>
##### Other materials
Development notes {% include navigation/pagelink.md folder=site.about name='archive' tag='archive' %}.
