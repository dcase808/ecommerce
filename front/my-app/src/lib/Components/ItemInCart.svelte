<script>
    import ItemWithQuantity from "$lib/Components/ItemWithQuantity.svelte";
    export let id, quantity;
    
    const getItems = async () => {
        return await fetch("https://ecommerce-demo-api.herokuapp.com/v1/api/items/" + id)
        .then(response => response.json())
        .then(response => response) 
    } 
    let item = getItems()
</script>
<main>
	{#await item}
		<span>Loading</span>
	{:then item} 
			<ItemWithQuantity id={item._id} title={item.title} price={item.price} img={item.img} desc={item.desc} quantity={quantity}/>
	{/await}
</main>
<style>
    main {
		margin: auto;
		display: flex;
		flex-direction: column;
	}
</style>