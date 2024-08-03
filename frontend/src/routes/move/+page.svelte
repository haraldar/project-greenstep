<script>
	import { minsToMeterRadius } from '$lib/utils';
	import { Button } from '$lib/components/ui/button';
	import Map from '$lib/components/Map.svelte';
</script>

<div class="flex h-full w-full flex-grow flex-col items-center justify-center">
	<div class="pb-2 text-center text-2xl font-bold">Move a little!</div>
	<div class="">
		<Map
			radius={minsToMeterRadius(49, 15)}
			categoryFilter="kultur sehenswürdigkeiten,anderes/parks und grünanlagen,anderes/stadtrundgang"
		/>
	</div>
	<div class="pt-5"><Button href="/">Next</Button></div>
</div>
