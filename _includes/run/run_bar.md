<table width="100%">

<tr>
{% for run in site.runs %}
{% assign button_title=run.title | replace: "Run ", "" %}
<td align="center">
  {% if run.title==page.title %}
  <a href="{{ run.url | relative_url }}" class="btn btn-primary btn-sm active" role="button" aria-pressed="true">{{ button_title }}</a>
  {% else %}
  <a href="{{ run.url | relative_url }}" class="btn btn-primary btn-sm" role="button" aria-pressed="true">{{ button_title }}</a>
  {% endif %}
</td>
{% endfor %}

</tr>
</table>
