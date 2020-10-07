{% include_cached run/run_bar.md %}
<hr/>
<center><h2>{{ page.title }}</h2></center>
<hr/>

{% assign images = site.data.gallery | where: "type", "run_configuration" | where: "run", include.run %}
{% assign length = images | size %}

{% if length!=0 %}
{% assign image=images[0].path %}
{% assign title=images[0].title %}
{% assign width=images[0].width %}


<table width="110%">
<tr><th style="text-align:center">Configuration Diagram</th><th style="text-align:center">RHIC+PHENIX Run Records</th></tr>
<tr>
<td><hr/></td><td><hr/></td>
</tr>

<tr>

<td style="text-align:center">
{% if image!='' %}
{% include images/include_image.md image=image title='' width=width %}
{% else %}
&nbsp;
{% endif %}
</td>

<td valign="top">
{% include rhic/rhic_record.md run=include.run %}
</td>

</tr>

</table>

{% endif %}

{% include_cached rhic/lumi_page.md run=include.run %}
