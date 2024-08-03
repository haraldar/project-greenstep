<script>
	import { Button } from '$lib/components/ui/button';
</script>

<div class="flex h-full w-full flex-grow flex-col justify-center">
	<div class="w-full py-10 text-center text-3xl font-bold">What do you want to do now?</div>
	<div class="flex flex-col justify-center gap-6 p-6">
		{#each ['Eat', 'Move', 'Explore'] as title}
			<Button class="rounded-3xl p-9 text-2xl" href={`/${title.toLowerCase()}`}>{title}</Button>
		{/each}
	</div>
</div>
