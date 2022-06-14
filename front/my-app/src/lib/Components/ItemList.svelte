<script>
     const getItems = async () => {
        const response = await fetch('https://ecommerce-demo-api.herokuapp.com/v1/api/items')
        return await response.json();
    } 
    const items = getItems();
</script>

<div class="menu">
    <div class="items">
        <ul>
        {#await items}
            loading
        {:then items}
        {#each items as item }
        <li>
            <a href= {`/items/${item._id}`}>{item.title}</a>
            <br>
        </li>
        {/each}
        {:catch error}
        <p>{error}</p>
        {/await}
        </ul>
    </div>
</div>

<style>
    .menu {
        text-align: left;
        width: 100%;
    }
    .items {
        padding: 10px 16px;
        margin: 20px 0;
        border-bottom: 1px solid #fafafa;
        font-size: 20px;
    }

</style>