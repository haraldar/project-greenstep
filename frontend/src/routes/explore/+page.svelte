<script>
	import { minsToMeterRadius } from '$lib/utils';
	import { Button } from '$lib/components/ui/button';
	import Map from '$lib/components/Map.svelte';
	import { SquareCheck } from 'lucide-svelte';
</script>

<div class="flex h-full w-full flex-grow flex-col items-center justify-center">
	<div class="flex items-center gap-3 pb-3 text-center text-xl">
		<span class="pr-2"><SquareCheck /></span><span class="pr-2 font-bold">5 / 35</span> city checkpoints
	</div>
	<div class="">
		<Map
			radius={minsToMeterRadius(49, 15)}
			categoryFilter="kultur sehenswürdigkeiten,anderes/parks und grünanlagen,anderes/stadtrundgang"
		/>
	</div>
	<div class="pt-5"><Button href="/">Next</Button></div>
</div>
