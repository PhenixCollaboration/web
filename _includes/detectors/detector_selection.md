<center>
<table WIDTH="100%">

<tr><th>Name</th><th>Role</th></tr>

{% assign detectors = site.data.detectors | where: "category", include.category %}

{% for detector in detectors %}
{% assign page = site.detectors | where: "name", detector.name | first %}
{% include detectors/detector_link.md page=page detector=detector %}
{% endfor %}

</table>
</center>
