<script>
    import { shopping_cart } from '$lib/stores.js'
    import ItemInCart from '$lib/Components/ItemInCart.svelte';

    let cart;

    shopping_cart.subscribe(value => {
        cart = value
    })


</script>

<main>
    {#each cart as item}
        <ItemInCart id={item.item_id} quantity={item.quantity}/>
    {/each}
</main>
<style>
    main{
        width: 70%;
        margin: auto;

    }
</style>