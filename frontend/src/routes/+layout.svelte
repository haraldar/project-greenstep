<script>
	import '../app.css';
	import '@fontsource-variable/inter';
	import { AudioWaveform, BatteryCharging, Clock2, Diamond, Scan, ScanQrCode } from 'lucide-svelte';
	import { Button } from '$lib/components/ui/button';
	import * as Drawer from '$lib/components/ui/drawer/index.ts';
	import * as Avatar from '$lib/components/ui/avatar/index.ts';
</script>

<div class="main-div flex h-[100vh] w-[100vw] flex-col">
	<div class="flex w-full justify-between rounded-b-3xl bg-gray-900 px-3 pb-4">
		<div class="flex items-center gap-2 pl-2 pt-3">
			<Diamond class="font-black text-amber-300" /><span class="pl-1 text-white"
				><span class="font-bold">9</span> EVEE</span
			>
		</div>
		<div class="pt-3">
			<div
				class="flex items-center justify-center gap-2 rounded-3xl bg-gray-50 p-3 px-8 pt-3 text-sm"
			>
				<Clock2 /> <span>28 min</span>
			</div>
		</div>
		<div class="pl-4 pr-3 pt-3">
			<Avatar.Root>
				<Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
				<Avatar.Fallback>CN</Avatar.Fallback>
			</Avatar.Root>
		</div>
	</div>
	<div class="flex h-full w-full flex-grow">
		<slot></slot>
	</div>
	<nav
		class="rounded- flex justify-between rounded-t-3xl border-t border-gray-300 bg-gray-900 p-3 px-8"
	>
		<Button class="text-xl"><BatteryCharging href="/charge" /></Button>
		<Drawer.Root class="bg-gray-900">
			<div class="bg-gray-900">
				<Drawer.Trigger asChild let:builder>
					<Button builders={[builder]} class="text-xl"><AudioWaveform /></Button>
				</Drawer.Trigger>
				<Drawer.Content class="bg-gray-900">
					<div class="h-[70vh] w-full bg-gray-700">
						<Drawer.Header>
							<Drawer.Title ii>Eve - your EV station assistant</Drawer.Title>
							<Drawer.Description>Set your daily activity goal.</Drawer.Description>
						</Drawer.Header>
						<div class="flex h-full flex-grow"></div>
						<Drawer.Footer class="pb-8">
							<Drawer.Close asChild let:builder>
								<Button builders={[builder]} class="text-xl"><AudioWaveform /></Button>
							</Drawer.Close>
						</Drawer.Footer>
					</div>
				</Drawer.Content>
			</div>
		</Drawer.Root>
		<Button class="text-xl"><ScanQrCode href="/scan" /></Button>
	</nav>
</div>

<style>
	.main-div {
		background: #abbaab; /* fallback for old browsers */
		background: -webkit-linear-gradient(
			to right,
			#ffffff,
			#abbaab
		); /* Chrome 10-25, Safari 5.1-6 */
		background: linear-gradient(
			to right,
			#ffffff,
			#abbaab
		); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
		background: #efefbb; /* fallback for old browsers */
		background: -webkit-linear-gradient(
			to right,
			#d4d3dd,
			#efefbb
		); /* Chrome 10-25, Safari 5.1-6 */
		background: linear-gradient(
			to right,
			#d4d3dd,
			#efefbb
		); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
	}
</style>
