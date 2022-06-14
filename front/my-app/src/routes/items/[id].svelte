<script>  
    import { page } from '$app/stores';
    import { shopping_cart } from '$lib/stores.js'
    
    let cart;

    shopping_cart.subscribe(value => {
        cart = value
    })

    let id = $page.params.id;
    const getItems = async () => {
        return await fetch("https://ecommerce-demo-api.herokuapp.com/v1/api/items/" + id)
        .then(response => response.json())
        .then(response => response)
        
    } 
    const addToCart = () => {
        if (cart.some(e => e.item_id === id)) 
        {
            cart.some(e => {
                e.quantity = e.quantity + 1
            })
        }
        else
        {
            cart.push({
                item_id: id,
                quantity: 1
            })
        }
    }
    const item = getItems();
    </script>
<main>
    {#await item}
        <span>loading</span>
    {:then item} 
        <div class='img'>
            <img src={item.img} alt={item.title + ' img'} class='item_img'>
        </div>
        <div class='summary'>
            <div class='title'>{item.title}</div>
            <div class='price'>{item.price} PLN</div>
            <div class='description'>{item.desc}</div>
            <div class='add-to-cart'><button on:click={addToCart}>Dodaj do koszyka</button></div>
        </div>
        
    {/await}
</main>
<style>
    main {
        margin: auto;
        width: 70%;
        display: flex;
        align-items: center;
    }
    .add-to-cart {
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .img  {
        height: 300px;
        width: 300px
    }
    .item_img{
        width: 300px;
    }
    .summary {
        margin-top: 20px;
        margin-left: 20px;
    }
    .title {
        font-size: 20px;
        font-weight: bold;
    }
    .description {
        margin-top: 10px;
    }
    button {
        width: 200px;
        height: 50px;
        border: none;
    }
</style>