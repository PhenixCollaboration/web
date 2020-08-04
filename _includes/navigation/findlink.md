{%- if include.title -%}
{%- assign tag=include.title -%}
{%- endif -%}
{%- if include.tag -%}
{%- assign tag=include.tag -%}
{%- else -%}
{%- assign tag=include.name -%}
{%- endif -%}
{%- assign found_items=site.data.links | where: "name", include.name -%}
{%- if include.category %}
{%- assign found_items=found_items | where: "category", include.category | compact -%}
{%- endif -%}
{%- assign found_link= found_items | map: "url" | first -%}
{%- if found_link -%}
{%- if include.category -%}
* [{{ tag }}]({{ found_link }}){:target="_blank"}
{%- else -%}
[{{ tag }}]({{ found_link }}){:target="_blank"}
{%- endif -%}
{%- endif -%}
