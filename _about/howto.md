---
title: How to Contribute
layout: newbase
abbrev: howto
weight: 10
level: 0
---
{% assign find_site_page=site.about | where: "abbrev", 'site' %}
{% assign site_page_url=find_site_page[0].url  | relative_url %}

{% assign find_contacts_page=site.about | where: "abbrev", 'contact' %}
{% assign contacts_page_url=find_contacts_page[0].url  | relative_url %}

{% include title.md %}

### Welcome
Contributions from the PHENIX community are crucial for this project to succeed.
You are most welcome to get involved. Materials that you consider to be relevant
to the mission of the site can be sent for consideration to the members of the
<a href="{{ contacts_page_url }}">Data and Analysis Preservation task force</a>.

### Direct Contributions
If you are willing to contribute directly by developing the actual content
this will be even more valuable and greatly appreciated. For this, you will
need to have basic knowledge of the Web platform used on this <a href="{{ site_page_url }}">site</a>.
This assumes that you are familiar with the following:
* Basic features of *git*.
* <a href="https://www.github.com/">GitHub</a>. You may also want to familiarize yourself with handling
a "fork" (your copy of the repository) and the mechanics of the "pulls request"
(process in which your changed - made in the fork) are merged into the master repo.
* The <a href="https://www.markdownguide.org/basic-syntax/">Markdown Syntax</a> (which is really not hard at all).

For optimal productivity, you should install the <a href="http://jekyllrb.com/">Jekyll</a> web
site generator on your laptop or workstation which will allow you to test drive the updated site
 e.g. after you make a few edits, before commit your changes to the repository.
The more adventerous and/or expert users can leverage the following components of the platform:
* The <a href="https://shopify.github.io/liquid/">Liquid</a> template language - for creating original pages on this site
* The <a href="http://getbootstrap.com/">Bootstrap</a> toolkit - for modifying layouts of web pages and their behavior

The latter two items are optional.

Please take a look at the <a href="{{ site.github }}" target="_blank">repository</a>
to get an idea of the general organization of the data, layouts and supporing logic.
The idea is to shape the code and content in a way that is easy to navigate
and modify. The following sections explain how this is achieved.
Development of this site involves the following aspects:
* adding and modifying the structured data content
* adding "assets" i.e. documents, images etc - although this needs to be done sparingly: one
needs to keep in mind that there are practical limits on the size of any repository, as well
as hard limits on repositories of sites which are hosted as "GitHub pages"
* interfacing the navigation tools on this site, which for the most part consists
of the top navigation bar and the dropdown menus

### Site Mechanics

#### The Navigation Bar
Entries in the navigation bar on top are named in a manner
consistent with the names of the folders in this project, for example the "EIC" entry in the navigation
bard is a dropdown menu with the content defined in the "_eic" folder, "Software" is associated with the
folder "_software". These folders are treated as "collections" by the Jekyll framework and they need
to be declared in the main configuration file
<a href="{{ site.github }}/blob/master/_config.yml" target="_blank">_config.yml</a>.

The top-level entries (and therefore the folders) included in the navigation bar are defined in a concise way in its
<a href="{{ site.github }}/blob/master/_includes/navbar_updated.ext" target="_blank">code</a>.

#### Dropdown Menus
The dropdown menus in the navigation bar are populated automatically based on the content of respective folders
(called "collections" in the Jekyll framework). This site's design uses the following conventions:
* each folder contains a collection of Markdown-formatted ("MD") files
* in general each file will be mapped to an entry in the dropdown menu
* each MD file is expected to be equipped with the "front matter" section
* each MD file can be either
   * the source for the page referenced in the respective dropdown menu entry
   * rendered as a common link to an external resource if there is a *"link"* attribute in the "front matter" section of that file
* the ordering of items in the menu is defined by the "weight" attribute in the "front matter" section, with smaller weights on top and larger on the bottom
* to include a divider right above an entry in a dropdown menu the following entry should be added
to the front matter: "*div: yes*"

#### Managing Data
Jekyll is fairly flexible when it comes to storing and manipulating structured data.
The data component of the site can reside in the "front matter" section of the Markdown-formatted
files or in separate YAML (or JSON, CSV etc) data sources. The front matter approach works well
for small sites. For scalability, it is recommended to rely mostly on dedicated data files (i.e.
files in the "<a href="{{ site.github }}/tree/master/_data" target="_blank">_data</a>" folder)
and keep the content of the front matter sections of individual MD files to a minimum.

The <a href="https://shopify.github.io/liquid/" target="_blank">Liquid</a> template language
features a variety of filters that can be applied to the data stored in YAML and other data sources
as well as in the front matter blocks of pages, and decent (not perfect) support for collections,
iterators and flow control constructs.

Information assets on this site (e.g. imaged, PDF files etc) are stored in the aptly named
"<a href="{{ site.github }}/tree/master/assets/" target="_blank">assets</a>"
folder and its subsiduaries. This convention should be kept going forward.

#### Formatting
We aim to provide a uniform look and feel across the site. To that end, whenever possible
the head (title) of each page is formatted by using the standard include layouts/title.md - please
look a the code for examples of its use. It's renders the page title from the front matter sections.

Headers of sections within a page are currently formatted in Markdown as "header level 4" i.e. prepended
with four hash characters like in **"#### My section header"**. Take a look at the header (Formatting)
of this section to get an idea of how it's rendered.

#### Development

To productively participate in the development of this site one needs to learn the
<a href="http://jekyllrb.com/">Jekyll</a> framework and perform its installation on
a development machine. This way any modification can be validated immediately since
the locally running development server provided by Jekyll will render the site
on the local host. Basic knolwede of the <a href="https://shopify.github.io/liquid/" target="_blank">
Liquid</a> template language and in particular the "filters" that are part of it is extremely helpful.
