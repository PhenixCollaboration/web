{% if include.title %}
##### {{ include.title }}
{% endif %}

{% assign items = site.data.documents | where: "category", include.category %}
{% if include.type %}
{% assign items = items | where: "type", include.type %}
{% endif %}
{% for item in items %}
{% if item.format=='markdown_link' %}
* {{ item.name }}{:target="_blank"}&nbsp; &nbsp; {{ item.title }}
{% else %}
* [{{ item.title }}]({{ site.document_folder | append: item.name | relative_url }}){:target="_blank"}
{% comment %}
  <li><a href="{{ site.document_folder | append: item.name | relative_url }}" target="_blank">{{ item.title }}</a></li>
{% endcomment %}
{% endif %}
{% endfor %}

