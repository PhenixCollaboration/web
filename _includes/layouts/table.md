{% if include.width %}
{% assign width=include.width %}
{% else %}
{% assign width='100%' %}
{% endif %}

<table border="1" width="{{ width }}">
  {% assign headers = include.headers | split: ", " %}
  <tr>
    {% for header in headers %}
    <th>{{ site.tablepadding }}{{ header }}</th>
    {% endfor %}
  </tr>
  {% for row in include.rows %}
  <tr>
    {% assign columns = row | split: ", " %}
    {% for item in columns %}
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
