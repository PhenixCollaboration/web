{% assign found_page=site.about | where: "name", include.name | map: "url" | first | relative_url %}
