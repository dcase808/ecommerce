<script>
	import Item from "$lib/Components/Item.svelte";
	const getItems = async () => {
        const response = await fetch('https://ecommerce-demo-api.herokuapp.com/v1/api/items')
        return await response.json();
    } 
    const items = getItems();
</script>
<main>
	{#await items}
		<span>Loading</span>
	{:then items} 
		{#each items as item}
			<Item id={item._id} title={item.title} price={item.price} img={item.img} desc={item.desc}/>
		{/each}
	{/await}
</main>

<style>
	main {
		margin: auto;
		width: 70%;
		display: flex;
		flex-direction: column;
	}
</style>
