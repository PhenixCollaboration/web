<table width="100%">

{% comment %}
{% tablerow run in site.runs cols:16 %}
<a href="{{ run.url | relative_url }}">{{ run.title }}</a>
{% endtablerow %}
{% endcomment %}

<tr>
{% for run in site.runs %}
<td align="center">
  {% if run.title==page.title %}
  <a href="{{ run.url | relative_url }}" class="btn btn-primary btn-sm active" role="button" aria-pressed="true">{{ run.title | replace: "Run ", "" }}</a>
  {% else %}
  <a href="{{ run.url | relative_url }}" class="btn btn-primary btn-sm" role="button" aria-pressed="true">{{ run.title | replace: "Run ", "" }}</a>
  {% endif %}
</td>
{% endfor %}

</tr>
</table>
