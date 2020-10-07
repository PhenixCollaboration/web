<table width="100%">

<tr>

{% for run in site.runs %}
{% assign button=run.title | replace: "Run ", "" %}

{% if run.title==include.title %}{% assign active='active' %}{% else %}{% assign active='' %}{% endif %}
<td align="center">
<a href="{{ run.url | relative_url }}" class="btn btn-primary btn-sm {{ active }}" role="button" aria-pressed="true">{{ button }}</a>
</td>
{% endfor %}

</tr>
</table>
{{ thetitle }}
