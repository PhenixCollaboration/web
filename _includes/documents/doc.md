{% if include.title %}
##### {{ include.title }}
{% endif %}


{% if include.category %}
{% assign items = site.data.documents | where: "category", include.category %}
{% else %}
{% assign items = site.data.documents %}
{% endif %}

{% if include.type %}
{% assign items = items | where: "type", include.type %}
{% endif %}

{% if include.venue %}
{% assign items = items | where: "venue", include.venue %}
{% endif %}

{% if include.name %}
{% assign items = items | where_exp: "item", "item.name==include.name" %}
{% endif %}

{% if include.tag %}
{% assign dummy = "" | split: "" %}
{% for item in items %}
{% if item.tags contains include.tag %}
{% assign dummy=dummy | push: item %}
{% endif %}
{% endfor %}
{% assign items=dummy %}
{% endif %}


{%- for item in items -%}
{%- if item.format=='markdown_link' -%}
{%- if item.resource=='zenodo' %}
* {% include_cached navigation/zenodo.md item=item %}

{%- elsif item.resource=='hepdata' -%}
* {% include_cached navigation/hepdata.md item=item %}
{%- else -%}
* {% include_cached navigation/generate_md_link.md item=item %}
{%- endif -%}

{%- else %}
* [{{ item.title }}]({{ site.document_folder | append: item.name | relative_url }}){:target="_blank"}
{%- endif %}
{%- endfor -%}

{% comment %}
  <li><a href="{{ site.document_folder | append: item.name | relative_url }}" target="_blank">{{ item.title }}</a></li>
{% endcomment %}


