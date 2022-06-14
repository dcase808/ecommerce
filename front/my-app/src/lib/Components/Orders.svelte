<script>
    import ItemInOrders from './ItemInOrders.svelte';
    export let _id, item, price, paid
</script>

<div class="Orders">
    <p>ID produktu: {_id}</p>
        {#each item as it}
            <ItemInOrders id ={it.id} quantity = {it.quantity} />
        {/each}   
    <p> class='price'>Cena: {price}</p>
    <p>Czy zapłacono? {paid}</p>
</div>