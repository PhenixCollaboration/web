
{% assign title=page.title %}
{% assign alt_title=include.title %}

{% if alt_title and alt_title!='' %}
{% assign title = alt_title %}
{% endif %}

{% assign type=include.type %}
{% assign run=include.run %}
{% assign columns=include.columns %}

{% assign cols=2 %}
{% if columns %}
{% assign cols=columns %}
{% endif %}

{% assign gallery="main" %}
{% if include.gallery %}
{% assign gallery=include.gallery %}
{% endif %}

{% assign images = site.data.gallery | where: "type", type | where: "gallery", gallery | sort: 'weight' %}


{% if run and run!='' %}
{% assign images = images | where: "run", run %}
{% endif %}

{% assign length = images | size %}

{% if length!=0 %}
<h3> {{ title }} </h3>
<table width="100%">

{% tablerow image in images cols:cols %}

{% if image.title !='' %}
<b>{{ image.title }}</b><br/>
{% endif %}

<a href="{{ image.path | relative_url }}">
<img src="{{ image.path | relative_url }}" alt="{{ image.title}}" height="300px"/>&nbsp;<br/><p/>
</a>
{% endtablerow %}

</table>

{% endif %}
