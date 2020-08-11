---
layout: newbase
name: site
---
{% capture howto_page_url %}{% include navigation/findpage.md folder=site.about name='howto' %}{% endcapture %}

{% include layouts/find_title.md name=page.name %}

This website is under active development. If you are able and willing to contribute, your help will be greatly appreciated! There are a variety of work items for almost any skill level and area of expertise. Should you need to add or modify content on this site or some parts of its layout you will find the ['how-to' page]({{ howto_page_url }}) useful.

Please take a look at the following list and let us know if you can help:

<table border="1" width="100%">
  <tr>
    <th>{{ site.tablepadding }}Description</th>
    <th>{{ site.tablepadding }}Required Level of Expertise</th>
    <th>{{ site.tablepadding }}Priority</th>
  </tr>
  {% for item in site.data.work %}
  <tr>
    <td>{{ site.tablepadding }}{{ item.description }}</td>
    <td>{{ site.tablepadding }}{{ item.expertise }}</td>
    <td>{{ site.tablepadding }}{{ item.priority }}</td>
  </tr>
  {% endfor %}
  
</table>
