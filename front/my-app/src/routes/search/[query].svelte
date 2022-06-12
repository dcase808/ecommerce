<script>  
    import {page} from '$app/stores';
    let query = $page.params.query;
    const getItems = async () => {
        return await fetch('https://ecommerce-demo-api.herokuapp.com/v1/api/items/search?query=' + query)
        .then(response => response.json())
        .then(response => response)
    } 
    const items = getItems();
    
</script>

{#await items}
    loading
{:then items}
{#each items as item}
<a href= {`/items/${item._id}`}>{item.title}</a>
{/each} 
    
{/await}