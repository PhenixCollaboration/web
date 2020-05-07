---
abbrev: zdc
layout: newbase
image: '/images/detectors/phenix_quartercut_zdc.png'
image_title: 'PHENIX Quarter Cut with the ZDC highlighted'
category: event
---
{% include layouts/find_detector_title.md abbrev=page.abbrev %}
# {{ title }}

{% assign detector = page.abbrev %}
{% assign image = page.image %}
{% assign image_title = page.image_title %}

{% include images/include_image.md detector=detector image=image image_title=image_title width=450 %}
