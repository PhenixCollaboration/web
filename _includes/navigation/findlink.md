{%- if include.title -%}
{%- assign tag=include.title -%}
{%- else -%}
{%- assign tag=include.name -%}
{%- endif -%}
{%- assign found_items=site.data.links | where: "name", include.name -%}
{%- if include.category %}
{%- assign found_items=found_items | where: "category", include.category | compact -%}
{%- endif -%}
{%- assign found_link= found_items | map: "url" | first -%}
{%- assign found_comment=found_items | map: "comment" | first -%}
{%- if found_link -%}
{%- if include.category -%}
* [{{ tag }}]({{ found_link }}){:target="_blank"} {{ found_comment }}
{%- else -%}
[{{ tag }}]({{ found_link }}){:target="_blank"} {{ found_comment }}
{%- endif -%}
{%- endif -%}
