{% assign item=site.data.conferences | where: "name", include.name | first %}
##### {{ item.title }}
{% include navigation/findlink.md name=item.name tag='Conference Website' %}
{% assign docs=site.data.documents | where: "type", 'conference presentation' | where: "venue", include.name -%}

<table width="100%">
  {% for doc in docs %}
  <tr>
    <td width="15%"><b>{{ doc.author }}</b></td>
    <td width="65%">"{{ doc.title }}"</td>
    <td width="20%">{% include navigation/zenodo.md item=doc htmlbadge='yes' %}</td>
  </tr>
{% endfor %}
</table>

