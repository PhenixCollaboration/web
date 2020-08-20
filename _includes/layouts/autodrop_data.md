{% case include.what %}
{% when "collaboration" %}	{% assign theCollection=site.collaboration %} {% assign icon=site.collaboration_icon %}
{% when "experiment" %}		{% assign theCollection=site.experiment %} {% assign icon=site.experiment_icon %}
{% when "detectors" %}		{% assign theCollection=site.detectors %}  {% assign icon=site.detectors_icon %}
{% when "software" %}		{% assign theCollection=site.software %}   {% assign icon=site.software_icon %}
{% when "analysis" %}		{% assign theCollection=site.analysis %}   {% assign icon=site.analysis_icon %}
{% when "resources" %}		{% assign theCollection=site.resources %}  {% assign icon=site.resources_icon %}
{% when "about" %}		{% assign theCollection=site.about %}      {% assign icon=site.about_icon %}
{% endcase %}

{% comment %}
#######################################################################################
This is where we pick a particular dropdown menu which is a part
of the "navbar". The list of these dropdowns is traversed in the navbar,
and here we just fill each with its own content.

Note that "name" in submenu must match "name" in the front matter of the file, for
that file to be accessible from the dropdown.
#######################################################################################
{% endcomment %}

{% assign the_menu = site.data.menus | where: "name", include.what | first %}
{% assign target='' %}

<li class="nav-item dropdown px-4">
  {% if icon.size > 0 %}
  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="color: #fff;">{{ the_menu.full }}&nbsp;&nbsp;<img src="{{ icon | relative_url }}" height="24" width="24"></a>
  {% else %}
  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="color: #fff;">{{ the_menu.full }}</a>
  {% endif %}
  
<div class="dropdown-menu" aria-labelledby="navbarDropdown">

{% for submenu in the_menu.submenus %}{% if submenu.exclude %}{% continue %}{% endif %}

{% comment %}
First, handle external links
{% endcomment %}

{% if submenu.link %}
{% assign theLink=submenu.link %}
{% assign target=site.blank %}

{% else %}
{% comment %}
Now, internal links
{% endcomment %}

{% assign item=theCollection | where: "name", submenu.name | first %}
{% assign theLink=item.url | relative_url %}

{% endif %}

{% if submenu.div %}<div class="dropdown-divider"></div>{% endif %}

{% if submenu.label %}
<div class="dropdown-item" style="color: #fff; background-color: #888;">{{ submenu.full }}</div>
{% else %}
{% if submenu.icon %}
<a class="dropdown-item" href="{{ theLink }}" {{ target }}>{{ submenu.full }} &nbsp; <img src="{{ submenu.icon | relative_url}}" height="16"/></a>
{% else %}
<a class="dropdown-item" href="{{ theLink }}" {{ target }}>{{ submenu.full }}</a>
{% endif %}
{% endif %}

{% endfor %}

</div>
</li>

