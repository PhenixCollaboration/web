<table border="1" width="95%">
  <tr>
    <th>&nbsp;&nbsp;&nbsp;Type</th>
    <th>&nbsp;&nbsp;&nbsp;Name</th>
    <th>&nbsp;&nbsp;&nbsp;Description</th>
  </tr>
  {% for var in include.rows %}
  <tr>
    <td>&nbsp;&nbsp;&nbsp;{{ var.type }}</td>  
    <td>&nbsp;&nbsp;&nbsp;{{ var.name }}</td>  
    <td>&nbsp;&nbsp;&nbsp;{{ var.desc }}</td>  
  </tr>
  {% endfor %}
</table>
