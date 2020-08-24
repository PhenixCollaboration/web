<table width="120%">
  {% for who in site.data.dap_team %}
  {% if who.teams contains include.team %}
  <tr>
    <td width="25%">{{ who.full }}</td>
    <td width="15%"><a href="mailto:{{ who.email }}">{{ who.email }}</a></td>
    <td width="60%">{{ who.role }}</td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
