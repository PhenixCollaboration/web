{%- assign found_link=site.data.links | where: "name", include.name | map: "url" | first -%}
{%- assign found_comment=site.data.links | where: "name", include.name | map: "comment" | first -%}
* [{{ include.name }}]({{ found_link }}){:target="_blank"} {{ found_comment }}
