{% if include.width %}
{% assign width=include.width %}
{% else %}
{% assign width='100%' %}
{% endif %}

<table border="1" width="{{ width }}">
  <tr>
    {% for header in include.headers %}
    <th>{{ site.tablepadding }}{{ header }}</th>
    {% endfor %}
  </tr>
  {% for row in include.rows %}
  <tr>
    {% for item in row %}
    {% if item contains 'ERT_MASK' %}
    {% assign name = item | split: ":" | last %}
    <td>{{ site.tablepadding }}<a href="{{ site.ert_mask_folder | append: name | relative_url }}" {{ include.download }}>{{ name }}</a></td>
    {% else %}
    <td>{{ site.tablepadding }}{{ item }}</td>
    {% endif %}
    {% endfor %}
  </tr>
  {% endfor %}
  
</table>
