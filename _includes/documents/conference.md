{% assign item=site.data.conferences | where: "name", include.name | first %}
##### {{ item.title }}
{% include navigation/findlink.md name=item.name tag='Conference Website' %}
{% assign docs=site.data.documents | where: "type", 'conference presentation' | where: "venue", include.name -%}

<table width="100%">
  {% for doc in docs %}
  <tr>
    <td width="13%"><b>{{ doc.author }}</b></td>
    <td width="77%">"{% include navigation/zenodo_http.md item=doc %}"</td>
    <td width="10%">{% include navigation/zenodo.md item=doc htmlbadge='yes' %}</td>
  </tr>
{% endfor %}
</table>

