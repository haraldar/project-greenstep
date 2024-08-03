<script>
	import { Button } from '$lib/components/ui/button';
	import Map from '$lib/components/Map.svelte';
	import { onMount } from 'svelte';
	import { minsToMeterRadius } from '$lib/utils';

	const timeMap = {
		restaurant: 90,
		fastFood: 20,
		snack: 10
	};
</script>

<div class="flex h-full w-full flex-grow flex-col items-center justify-center">
	<div class="pb-2 text-center text-2xl font-bold">Grab some food!</div>
	<div class="">
		<Map radius={minsToMeterRadius(49, 15)} categoryFilter="essen trinken" />
	</div>
	<div class="pt-5"><Button href="/">Next</Button></div>
</div>
