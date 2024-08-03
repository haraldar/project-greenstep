<script>
	import '../app.css';
	import '@fontsource-variable/inter';
	import {
		AudioWaveform,
		BatteryCharging,
		Clock2,
		Diamond,
		Mic,
		Play,
		Scan,
		ScanQrCode
	} from 'lucide-svelte';
	import { Button } from '$lib/components/ui/button';
	import * as Drawer from '$lib/components/ui/drawer/index.ts';
	import * as Avatar from '$lib/components/ui/avatar/index.ts';
	import { ScrollArea } from '$lib/components/ui/scroll-area';

	let textarea;

	function resizeTextarea() {
		textarea.style.height = 'auto';
		textarea.style.height = Math.min(textarea.scrollHeight, 120) + 'px';
	}

	function handleInput() {
		resizeTextarea();
	}

	function handleScroll() {
		if (textarea.scrollHeight > 120) {
			textarea.style.overflowY = 'auto';
		} else {
			textarea.style.overflowY = 'hidden';
		}
	}

	const firstMessage = `You are a EVE - Electric Vehicle Charging Station Assistant - a helpful assistant that helps people at an electronic vehicle charging station. You are kind and helpful.
You also help people find interesting activities to do while they wait close to you.
Your suggestions depend on the remaining time the user has to wait for their vehicle to charge, the currently available events and on the location. You politely decline requests unrelated to the charging station.`;

	let messages = [{ role: 'system', content: firstMessage }];

	import OpenAI from 'openai';

	const openai = new OpenAI({
		dangerouslyAllowBrowser: true,
		organization: 'org-0Whneo6JCGdygEiMyatZwTAg',
		project: 'thesis',
		apiKey:
			'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'
	});

	async function ask(msgs) {
		const completion = await openai.chat.completions.create({
			messages: msgs,
			model: 'gpt-4o'
		});
		messages = [...messages, completion.choices[0]];
	}

	let chatContent = '';

	async function addMessage() {
		messages = [...messages, { role: 'user', content: chatContent }];
		chatContent = '';
		await ask(messages);
	}
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
					<div class="flex h-[85vh] w-full flex-grow flex-col justify-center bg-gray-700">
						<Drawer.Header>
							<Drawer.Title class="text-xl text-white">EVE</Drawer.Title>
							<Drawer.Description>Your helpful EV station assistant</Drawer.Description>
						</Drawer.Header>
						<div class="flex h-full flex-grow justify-center">
							<div class="h-full w-[410px]">
								<ScrollArea class="h-[60vh]">
									<div class="flex flex-grow flex-col gap-4 p-4">
										{#each messages.slice(1) as message}
											<div
												class={`flex ${message.role === 'assistant' ? 'justify-end' : 'justify-start'}`}
											>
												<div
													class="max-w-[70%] rounded-3xl px-5 py-2.5"
													class:bg-gray-200={message.role === 'user'}
													class:bg-blue-200={message.role === 'assistant'}
												>
													{message.text}
												</div>
											</div>
										{/each}
									</div></ScrollArea
								>
							</div>
						</div>
						<Drawer.Footer class="pb-4">
							<div class="flex items-end gap-2">
								<div class="relative w-full">
									<textarea
										class="rounded-3xl bg-gray-800 px-4 py-3 pr-8 text-sm text-white"
										rows="1"
										bind:this={textarea}
										on:input={handleInput}
										on:scroll={handleScroll}
										bind:value={chatContent}
									></textarea>
									<span class="absolute bottom-[10px] right-[12px]"
										><Button
											class="bg-transparent text-xs text-gray-300"
											size="xs"
											on:click={addMessage}><Play /></Button
										></span
									>
								</div>
								<div class="pb-1.5">
									<Button class="h-10 w-10 rounded-2xl" size="icon"><div><Mic /></div></Button>
								</div>
							</div>
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
	textarea {
		width: 100%;
		min-height: 32px;
		max-height: 120px;
		resize: none;
		overflow-y: hidden;
		box-sizing: border-box;
	}
</style>
