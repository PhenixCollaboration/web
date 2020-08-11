{% for item in site.data.documents %}
{% if item.tags contains include.tag %}
* {{ item.name }} {{ item.title }}
{% endif %}
{% endfor %}
