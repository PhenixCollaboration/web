{% assign docs=site.data.documents | where: "type", 'conference presentation' | where: "venue", include.name -%}
{% if include.width %}
<table width="{{ include.width }}">
{% else %}
<table width="100%">
{% endif %}
{% for doc in docs %}
  <tr>
    <td width="13%"><b>{{ doc.author }}</b></td>
    <td width="77%">"{% include navigation/zenodo_http.md item=doc %}"</td>
    <td width="10%">{% include navigation/zenodo.md item=doc htmlbadge='yes' %}</td>
  </tr>
{% endfor %}
</table>

