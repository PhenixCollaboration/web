{% case include.what %}
{% when "experiment" %}	{% assign theCollection=site.experiment %}
{% when "detectors" %}	{% assign theCollection=site.detectors %}
{% when "software" %}	{% assign theCollection=site.software %}
{% when "analysis" %}	{% assign theCollection=site.analysis %}
{% when "resources" %}	{% assign theCollection=site.resources %}
{% when "about" %}	{% assign theCollection=site.about %}
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
<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="color: #fff;">{{ the_menu.full }}</a>
<div class="dropdown-menu" aria-labelledby="navbarDropdown">

{% for submenu in the_menu.submenus %}{% if submenu.exclude %}{% continue %}{% endif %}

{% if submenu.link %}
{% assign theLink=submenu.link %}
{% assign target=site.blank %}

{% else %}

{% assign item=theCollection | where: "name", submenu.name | first %}
{% assign theLink=item.url | relative_url %}

{% endif %}

{% if submenu.div %}<div class="dropdown-divider"></div>{% endif %}

{% if submenu.label %}
<div class="dropdown-item" style="color: #fff; background-color: #888;">{{ submenu.full }}</div>
{% else %}
<a class="dropdown-item" href="{{ theLink }}" {{ target }}>{{ submenu.full }}</a>
{% endif %}

{% endfor %}

</div>
</li>

