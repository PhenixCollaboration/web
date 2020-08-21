{% assign items = site.data.gallery %}
{% if include.name %}
{% assign image = items | where: "name", include.name | first %}
{% endif %}

{% assign width='450' %}
{% if layout.image_width %}
{% assign width=layout.image_width %}
{% endif %}
{% if include.width %}
{% assign width=include.width %}
{% endif %}

<img src="{{ image.path | relative_url }}" width="{{ width }}px"/>



