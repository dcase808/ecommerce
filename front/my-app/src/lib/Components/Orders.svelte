<script>
    import ItemInOrders from './ItemInOrders.svelte';
    export let _id, item, price, paid
</script>

<section>
    <p>ID zamówienia: {_id}</p>
        {#each item as it}
            <ItemInOrders id ={it.id} quantity = {it.quantity} />
        {/each}   
    <p>Suma: {price} PLN</p>
    <p>Czy zapłacono? {paid}</p>
</section>
<style>
    section {
        border-bottom: solid 2px;
    }
</style>