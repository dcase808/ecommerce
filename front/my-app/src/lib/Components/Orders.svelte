<script>
    import ItemInOrders from './ItemInOrders.svelte';
    export let _id, item, price, paid
</script>

<div>
    <p>{_id}</p>
        {#each item as it}
            <ItemInOrders id ={it.id} quantity = {it.quantity} />
        {/each}   
    <p>{price}</p>
    <p>{paid}</p>
</div>