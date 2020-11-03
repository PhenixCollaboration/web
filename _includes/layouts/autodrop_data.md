{% case include.what %}
{% when "test" %}		{% assign theCollection=site.test %} 	{% assign icon=site.test_icon %}
{% when "collaboration" %}	{% assign theCollection=site.collaboration %} {% assign icon=site.collaboration_icon %}
{% when "experiment" %}		{% assign theCollection=site.experiment %} {% assign icon=site.experiment_icon %}
{% when "detectors" %}		{% assign theCollection=site.detectors %}  {% assign icon=site.detectors_icon %}
{% when "software" %}		{% assign theCollection=site.software %}   {% assign icon=site.software_icon %}
{% when "analysis" %}		{% assign theCollection=site.analysis %}   {% assign icon=site.analysis_icon %}
{% when "results" %}		{% assign theCollection=site.results %}    {% assign icon=site.results_icon %}
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
  {% assign the_icon='' %}
  {% if icon.size > 0 %}
  {% assign icon_url= icon | relative_url %}
  {% assign the_icon='&nbsp;&nbsp;<img src="' | append: icon_url | append: '" height="24" width="24">' %}
  {% endif %}
  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="color: #fff;">{{ the_menu.full }}{{ the_icon }}</a>
  
<div class="dropdown-menu" aria-labelledby="navbarDropdown">

{% for submenu in the_menu.submenus %}{% if submenu.exclude %}{% continue %}{% endif %}


{% if submenu.link %}				{% comment %} ---- First, handle external links	{% endcomment %}

{% assign theLink=submenu.link %}{% assign target=site.blank %}

{% else %}					{% comment %} ---- Now, internal links		{% endcomment %}
{% assign target='' %}
{% assign item=theCollection | where: "name", submenu.name | first %}
{% assign theLink=item.url | relative_url %}

{% endif %}

{% if submenu.div %}<div class="dropdown-divider"></div>{% endif %}

{% if submenu.label %}
<div class="dropdown-item" style="color: #fff; background-color: #0062cc;">{{ submenu.full }}&nbsp;<img src="{{ site.dn_arrow_icon | relative_url }}" height="8" width="8"/></div>

{% elsif submenu.nested %}
<div class="btn-group dropright">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Dropright
  </button>
  <div class="dropdown-menu">
    <a class="dropdown-item" href="#">Action</a>
    <a class="dropdown-item" href="#">Another action</a>
    <a class="dropdown-item" href="#">Something else here</a>    <!-- Dropdown menu links -->
  </div>
</div>

{% else %}


{% assign the_icon='' %}
{% if submenu.icon %}
{% assign icon_url= submenu.icon | relative_url %}
{% assign the_icon='&nbsp;&nbsp;<img src="' | append: icon_url | append: '" height="16" width="16">' %}
{% endif %}

<a class="dropdown-item" href="{{ theLink }}" {{ target }}>{{ submenu.full }}{{ the_icon }}</a>

{% endif %}

{% endfor %}

</div>
</li>

