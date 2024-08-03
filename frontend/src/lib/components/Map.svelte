<script>
	export let categoryFilter = '';
	export let directions = '';
	export let lat = 46.4983;
	export let lon = 11.3548;
	export let radius = '';
	export let showradius = 'false';
	export let zoom = '10';

	$: componentString = `<odh-activity-poi category-filter="${categoryFilter}" directions language="en" lat="${lat}" lon="${lon}" radius="${radius}" showradius=true zoom="${zoom}" </odh-activity-poi>`;
</script>

<svelte:head>
	<script
		src="https://cdn.webcomponents.opendatahub.com/dist/0e5fbede-4a21-4dd3-bf85-7d2be71dfb12/bundle.js"
	>
	</script>
</svelte:head>

<div>
	<iframe
		class="rounded-3xl"
		frameborder="0"
		width="410"
		height="620"
		src={`https://api.webcomponents.opendatahub.com/preview/0e5fbede-4a21-4dd3-bf85-7d2be71dfb12/latest?attribs=${btoa(componentString)}`}
	>
	</iframe>
</div>
