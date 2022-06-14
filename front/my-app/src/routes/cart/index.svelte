<script>
    import { shopping_cart } from '$lib/stores.js'
    import ItemInCart from '$lib/Components/ItemInCart.svelte';
    import {goto} from '$app/navigation';

    const removeQuantity = (id) => {
        for (const obj of $shopping_cart) 
        {
            if (obj.item_id === id) 
            {

                obj.quantity--;
                $shopping_cart = $shopping_cart
                if(obj.quantity < 1)
                {
                    $shopping_cart = $shopping_cart.filter(e => {
                        return e.item_id != id;
                    })
                }
            }
        }
        console.log($shopping_cart)
    }
    const addQuantity = (id) => {
        for (const obj of $shopping_cart) 
        {
            if (obj.item_id === id) 
            {
                obj.quantity++;
                $shopping_cart = $shopping_cart
            }
        }
    }
    $: calculateSum = () => {
        let sum = 0
        for (const obj of $shopping_cart)
        {
            sum = sum + obj.quantity * obj.price
        }
        return sum
    }
    const goToSummary = () => {
        goto('/summary')
    }

</script>

<main>
    
    {#if $shopping_cart.length !== 0}
        {#each $shopping_cart as item}
        <section>
            <div class='item'>
                <ItemInCart id={item.item_id} quantity={item.quantity}/>
            </div>
            <div class='buttons'>
                <button class='change-quantity' on:click={() => {removeQuantity(item.item_id)}}>-</button><button class='change-quantity' on:click={() => {addQuantity(item.item_id)}}>+</button>
            </div>
        </section>
        {/each}
            <div class='summary'>Suma: {calculateSum().toFixed(2)} PLN <button class='go-to-payment' on:click={goToSummary}>Podsumowanie</button></div>
        {:else}
            <p>Koszyk jest pusty.</p>
    {/if}
</main>
<style>
    main{
        width: 70%;
        margin: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    section {
        width: 100%;
        display: flex;
        align-items: center;
    }
    .item{
        width: 80%;
    }
    .buttons{
        width: 20%;
        margin-left: 100px;
        margin-right: -500px;
    }
    .change-quantity{
        width: 50px;
        height: 50px;
        border: none;
    }
    .go-to-payment {
        border: none;
        height: 50px;
        width: 150px;
    }
    .summary {
        margin-left: auto;
        margin: 20px 0px 20px auto;
    }
</style>