{%- if include.item.cached_badge -%}
{%- assign badge=site.zenodo_badges | append: 'zenodo.' | append: include.item.name | append: '.svg' | relative_url -%}
{%- else -%}
{%- assign badge="https://zenodo.org/badge/DOI/10.5281/zenodo." | append: include.item.name | append: ".svg" -%}
{%- endif -%}
{%- if include.htmlbadge -%}
<a href="{{ site.zenodo_prefix }}{{ include.item.name }}" target="_blank"><img src="{{ badge }}"/></a>
{%- else -%}
[![{{item.name}}]({{ badge }})](https://doi.org/10.5281/zenodo.{{ include.item.name }}){:target="_blank"}&nbsp; &nbsp;{{ include.item.title }} ({{ include.item.author }})
{%- endif -%}
