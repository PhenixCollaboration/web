{% assign zs = site.data.documents | where: "resource", "zenodo" %}
{% for item in zs %}
{{ item.name }}
{% endfor %}




<div class="hidden">
	<script type="text/javascript">
			var images = new Array()
			function preload() {
				for (i = 0; i < preload.arguments.length; i++) {
					images[i] = new Image()
					images[i].src = preload.arguments[i]
				}
			}
						preload(
						"https://zenodo.org/badge/DOI/10.5281/zenodo.3840266.svg",
						"https://zenodo.org/badge/DOI/10.5281/zenodo.3887326.svg",
						)
	</script>
</div>
