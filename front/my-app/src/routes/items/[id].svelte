<script>  
    import {page} from '$app/stores';
    let id = $page.params.id;
    const getItems = async () => {
        return await fetch("https://ecommerce-demo-api.herokuapp.com/v1/api/items/" + id)
        .then(response => response.json())
        .then(response => response)
        
    } 
    const addToCart = () => [
        console.log('add to cart')
    ]
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
        </div>
        
    {/await}
</main>
<style>
    main {
        margin: auto;
        width: 70%;
        display: flex;
    }
    .item_img{
        width: 300px;
    }
    .summary {
        margin-top: 100px;
        margin-left: 20px;
    }
    .title {
        font-size: 20px;
        font-weight: bold;
    }
    .description {
        margin-top: 10px;
    }
</style>