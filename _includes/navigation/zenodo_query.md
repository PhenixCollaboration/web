{%- assign linkname=include.name -%}
{%- if include.tag -%}
{%- assign linkname=include.tag -%}
{%- endif -%}
{%- assign z_link='<a href="https://zenodo.org/communities/phenixcollaboration/search?page=1&size=20&q=%22' | append: include.name | append: '%22" target="_blank">' | append: linkname | append:'</a>' -%}
{{ z_link }}
