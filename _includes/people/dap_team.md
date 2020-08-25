<table width="120%">
  {% for who in site.data.dap_team %}
  {% if who.teams contains include.team %}
  <tr>
    <td width="20%">{{ who.full }}</td>
    <td width="20%" align="left"><a href="mailto:{{ who.email }}">{{ who.email }}</a></td>
    <td width="60%">{{ who.role }}</td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
