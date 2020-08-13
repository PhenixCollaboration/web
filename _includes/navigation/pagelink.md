{%- assign tag=include.name -%}
{%- if include.tag -%}
{%- assign tag=include.tag -%}
{%- endif -%}
{%- assign found_page=include.folder | where: "name", include.name | map: "url" | first | relative_url -%}
{%- if include.html -%}
<a href="{{ found_page }}">{{ tag }}</a>
{%- else -%}
[{{ tag }}]({{ found_page }})
{%- endif -%}
