<script>
    import {API_URL} from '$lib/Constans/Constans.svelte'
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
        <p>ID zamówienia: {item._id}</p>
        <p>Ilość: {quantity}</p>
    {/await}
</div>