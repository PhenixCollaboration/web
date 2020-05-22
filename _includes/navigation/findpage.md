{% assign found_page=site.about | where: "abbrev", include.abbrev | map: "url" | first | relative_url %}
