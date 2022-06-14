<script>
    import {API_URL} from '$lib/Constans/Constans.svelte'
    import Item from '$lib/Components/Item.svelte'
    export let id, quantity

    const getItem = async () => {
        let url = API_URL + '/items/' + id
        return await fetch(url)
        .then(response => response.json())
		.then(response => response)
		.catch(e => console.error(e))
    }

    let item = getItem()
</script>

<div class="ItemInOders">
    {#await item}
        Loading
    {:then item}
        {quantity} X <Item id={item._id} title={item.title} price={item.price} img={item.img} desc={item.desc}/>
    {/await}
</div>