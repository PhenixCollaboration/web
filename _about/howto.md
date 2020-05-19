---
title: How to Contribute
layout: newbase
abbrev: howto
name: howto
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
You may be familiar with this syntax if you even had to edit your README.md files on GitHub
or similar documents elsewhere.
* Basics of the <a href="https://shopify.github.io/liquid/">Liquid</a> template language.

For optimal productivity, you should install the <a href="http://jekyllrb.com/">Jekyll</a> web
site generator on your laptop or workstation which will allow you to test drive the updated site
 e.g. after you make a few edits, before commit your changes to the repository.
Expert users can leverage the following components of the platform:
* The <a href="https://shopify.github.io/liquid/">Liquid</a> template language which will help manuipulate and render structured data on the pages of this site
* The <a href="http://getbootstrap.com/">Bootstrap</a> toolkit - for modifying layouts and appearance of these web pages and their behavior

Please take a look at the <a href="{{ site.github }}" target="_blank">repository</a>
to get an idea of the general organization of the data, layouts and supporing logic.
The idea is to shape the code and content in a way that is easy to navigate
and modify. The following sections explain how this is achieved.
Development of this site involves the following aspects:
* adding and modifying the structured data content (which in practice means files in YAML format and the "front matter" in
individual Markdown files to be rendered on the site - which also happens to be YAML)
* adding "assets" i.e. documents, images etc - although this needs to be done sparingly: one
needs to keep in mind that there are practical limits on the size of any repository, as well
as hard limits on repositories of sites which are hosted as "GitHub pages"
* interfacing the navigation tools on this site, which for the most part consists
of the top navigation bar and the dropdown menus

### Site Mechanics

#### The Navigation Bar and Dropdown Menus
Entries in the navigation bar on top are named in a manner
similar to the names of the folders in this project, for example the "EIC" entry in the navigation
bard is a dropdown menu with the content defined in the "_eic" folder, "Software" is associated with the
folder "_software". These folders are treated as "collections" by the Jekyll framework and they need
to be declared in the main configuration file <a href="{{ site.github }}/blob/master/_config.yml" target="_blank">_config.yml</a> in order to be properly rendered into HTML.

The structure of the navigation bar and the content of the dropdown menus are described in
a dedicated YAML file <a href="{{ site.github }}/blob/master/_data/menus.yml" target="_blank">_data/menus.yml</a>.

#### Managing Data
Jekyll is flexible when it comes to storing and manipulating structured data.
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
