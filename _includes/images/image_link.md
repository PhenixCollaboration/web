
{%- assign image=site.data.gallery | where: 'tag', include.tag | first -%}

[{{ image.title }}]({{ image.path | relative_url }}){:target="_blank"}
