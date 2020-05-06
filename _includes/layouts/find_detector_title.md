{% assign found_detector=site.data.detectors | where: "abbrev", include.abbrev | first %}
{% assign title=found_detector.title %}
