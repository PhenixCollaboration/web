{% assign the_run = site.data.runs | where: "run", page.run | first %}
{{ the_run.title }}
{% if the_run.subruns %}
{% for subrun in the_run.subruns %}

{% assign lumi_title = the_run.title | append: ", " | append: subrun.name | append: " period: luminosity accumulation and related data" %}
{% include images/generic_gallery.md type="lumi" run=page.run tag=subrun.name title=lumi_title columns=3 %}
{% include images/generic_gallery.md type="lumi" run=page.run tag=subrun.name title=" " columns=1 gallery="aux" %}

{% endfor %}
{% else %}

{% assign lumi_title = page.title | append: " luminosity accumulation and related data" %}

{% include images/generic_gallery.md type="lumi" run=page.run title=lumi_title columns=3 %}
{% include images/generic_gallery.md type="lumi" run=page.run title=" " columns=1 gallery="aux" %}

{% endif %}
