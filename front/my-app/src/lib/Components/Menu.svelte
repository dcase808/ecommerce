<script>
     const getItems = async () => {
        const response = await fetch('https://ecommerce-demo-api.herokuapp.com/v1/api/items')
        return await response.json();
    } 
    const items = getItems();
</script>

<div class="menu">
    <p>Kategorie</p>
    <div class="items">
        <ul>
        {#await items}
            loading
        {:then items}
        {#each items as item }
        <li>
            {item.title}
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
    }
    .items {
        padding: 10px 16px;
        margin: 20px 0;
        border-bottom: 1px solid #fafafa;
        font-size: 20px;
    }

</style>