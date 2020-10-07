{% include_cached run/run_bar.md run=include.run title=include.title %}
<hr/>
<center><h2>{{ page.title }}</h2></center>
<hr/>

{% assign images = site.data.gallery | where: "type", "run_configuration" | where: "run", include.run | first %}
{% assign length = images | size %}

{% if length!=0 %}
{% assign image=images.path %}
{% assign title=images.title %}
{% assign width=images.width %}


<table width="110%">
<tr><th style="text-align:center">Configuration Diagram</th><th style="text-align:center">RHIC+PHENIX Run Records</th></tr>
<tr>
<td><hr/></td><td><hr/></td>
</tr>

<tr>

<td style="text-align:center">
{% if image!='' %}
{% include_cached images/include_image.md image=image title='' width=width %}
{% else %}
&nbsp;
{% endif %}
</td>

<td valign="top">
{% include_cached rhic/rhic_record.md run=include.run %}
</td>

</tr>

</table>

{% endif %}

{% if site.lumi=='yes' %}
{% include_cached rhic/lumi_page.md run=include.run %}
{% endif %}

