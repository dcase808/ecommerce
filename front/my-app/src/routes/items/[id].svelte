<script>  
    import {page} from '$app/stores';
    let id = $page.params.id;
    const getItems = async () => {
        return await fetch("https://ecommerce-demo-api.herokuapp.com/v1/api/items/" + id)
        .then(response => response.json())
        .then(response => response)
        
} 
    const item = getItems();
    </script>

{#await item}
    loading
{:then item} 
<div class="item">
    <h3>{item.title}</h3>
    <p>{item.desc}</p>
    <p>{item.price}</p>
</div>
{/await}
