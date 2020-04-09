# The PHENIX Collaboration Data and Analysis Preservation Website

This website is designed to further the goals of the long-term Data
and Analysis Preservation (DAP) of the PHENIX Collaboration.

The site is under heavy development and is not officially in produciton.
At present, and until firther notice, it is not expected to be 100% functional
or have immediately useful content.


# SCOPE

We use the Jekyll static site generator.

The site is intended to preserve curated documentation for the PHENIX experiment,
including technical write-ups on the PHENIX software and its infrastructure. It is not
a document server although it does host a limited number of documents (primarily in
PDF formats) and as well as some diagrams.

Please note that the static nature of the site also implies lack of common database
query functions at runtime, authentication and authorization etc. Where needed, such
services will be hosted separately and links will be provided.


# TECHNICAL

## For the Developer

Please see the "how-to" section in the "About" menu of the site for the
information being constantly updated.

## Gems
Pay attention to the following dependencies (need to be installed and
also included in the Gemfile in this folder):

```
gem "jekyll", "~> 4.0"
gem 'jekyll-mentions', '~> 1.5', '>= 1.5.1'
gem 'jekyll-sitemap', '~> 1.4'
gem 'jekyll-redirect-from', '~> 0.16.0'
```
...and a few others. The best source is likely https://rubygems.org/

## Serving static content without Jekyll server
Links will need to be converted:
```
wget --convert-links -r http://localhost:4000/web/
```
