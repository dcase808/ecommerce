<script>
    import ItemInOrders from './ItemInOrders.svelte';
    export let _id, item, price, paid
</script>

<section>
    <p>ID zamówienia: {_id}</p>
    <p>Status: {paid ? 'Opłacone' : 'Nie opłacone'}</p>
        {#each item as it}
            <ItemInOrders id ={it.id} quantity = {it.quantity} />
        {/each}   
    <p>Suma: {price.toFixed(2)} PLN</p>
    
</section>
<style>
    section {
        border-bottom: dotted 1px;
    }
</style>