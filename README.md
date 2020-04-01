# ATTENTION

**Work in Progress**

Until further notice this web site is in the inital stages of preparation and at present is not expected to
be 100% functional or have immediately useful content.


# SCOPE

This is a static site built using the Jekyll static site generator.

It is intended to preserve curated documentation for the PHENIX experiment,
including technical write-ups on the PHENIX software and its infrastructure. It is not
a document server although it does host a limited number of documents (primarily in
PDF formats) and as well as some diagrams.

Please note that the static nature of the site also implies lack of
native database query functions, authentication and authorization etc.
Where needed, such services will be hosted separately and links will be
provided.


# TECHNICAL

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
