{% for menu in site.data.menus %}

{% for submenu in menu.submenus %}
{% if submenu.name==include.name %}
{% assign found_title=submenu.full %}
{% break %}
{% endif %}
{% endfor %}

{% endfor %}

{% if found_title %}
### {{ found_title }}
{% else %}
### {{ page.title }}
{% endif %}
{{ site.hr }}
