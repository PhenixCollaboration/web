# The PHENIX Collaboration Data and Analysis Preservation Website

This website is designed to further the goals of the long-term Data
and Analysis Preservation (DAP) of the PHENIX Collaboration. It
leverages the following Web services, portals and frameworks:

* Zenodo -- state of the art digital repository at CERN
* HEPData -- an archive of numerical data published in papers
* REANA -- a platform for "reproducible analysis"
* OpenData -- a CERN portal with the capability to host packages consisting
of documentation, software and data, in order to capture and document
substantial parts of interesting analyses


# TECHNICAL

## For the Developer

The `GitHub Pages` version is the development version.
For the current production version of the site please
see phenix.bnl.gov. There is no set schedule for releases,
these are done "as required".

Please see the "how-to" section in the "About" menu of the site for the
information being constantly updated. We use the Jekyll static site generator
and the `Liquid` template language.

## Gems
Pay attention to the following dependencies (need to be installed and
also included in the Gemfile in this folder):

```bash
gem "jekyll", "~> 4.0"
gem 'jekyll-mentions', '~> 1.5', '>= 1.5.1'
gem 'jekyll-sitemap', '~> 1.4'
gem 'jekyll-redirect-from', '~> 0.16.0'
```
...and a few others. The best source is likely https://rubygems.org/

NB. When running a freshly installed instance of _jekyll_, you'll get
error messages concerning possibly missing gems. These are trivial to
install, e.g. running commands like

```bash
gem install jekyll-mentions
```

## The "Liquid" template language

Documentation on the `Liquid` template language is plentiful
and easy to locate on the Web.

A useful trick for concatenation of arrays in Liquid:

```{% assign all_hosts = "" | split: "" %}
{% for host in site.data.shared_hosts %}
  {% assign all_hosts = all_hosts | push: host %}
{% endfor %}
{% for host in site.data.paas_hosts %}
  {% assign all_hosts = all_hosts | push: host %}
{% endfor %}
```

## Serving static content without Jekyll server

The site content can be captured using `wget` or a similar utility. Once it's
done, it can be accessed statically on a local machine or copied to a different server.
Note that links will need to be converted:

```
wget --convert-links -r http://localhost:4000/web/
```
