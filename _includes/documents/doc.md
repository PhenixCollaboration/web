{% if include.title %}
<h3>{{ include.title }}</h3>
{% endif %}

{% assign items = site.data.documents | where: "category", include.category %}
{% if include.type %}
{% assign items = items | where: "type", include.type %}
{% endif %}

  {% for item in items %}
  {% if item.format=='markdown_link' %}
* {{ item.name }}&nbsp; &nbsp; {{ item.title }}
  {% else %}
  <li><a href="{{ site.document_folder | append: item.name | relative_url }}" target="_blank">{{ item.title }}</a></li>
  {% endif %}
  {% endfor %}

