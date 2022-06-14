<script>
    let title, desc, price, img, tags = []
    import Cookies from 'js-cookie'
    import {ADMIN_API_URL} from '$lib/Constans/Constans.svelte'
    import Item from "$lib/Components/Item.svelte";

    let showError = false;
    let addStatus = false;


    const getItems = async () => {
        let url = ADMIN_API_URL + '/items'
        return await fetch(url, {
        headers: {
            'Authorization': 'Bearer ' + Cookies.get('jwt-token-admin')}
        })
        .then(response => response.json())
        .then(response => response)
    } 

    const addItem = async () => {
        let url = ADMIN_API_URL + '/items'
        let entry = {
            'title' : title,
            'desc' : desc,
            'price' : price,
            'tags' : tags
        }
            console.log(entry)
    let response = await fetch(url, {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + Cookies.get('jwt-token-admin'),
            'Content-type': 'application/json'},
        body: JSON.stringify(entry)
        })
    if(response.ok)
    {
        addStatus = true;
        showError = false;
    }
    else {
        showError = true
    }
    }

    const items = getItems();



</script>
<div class="content">
    <div class="getItems"></div>
    {#await items}
		<span>Loading</span>
	{:then items} 
		{#each items as item}
			<Item id={item._id} title={item.title} price={item.price} img={item.img} desc={item.desc}/>
		{/each}
	{/await}
    <div class="addItem">
        {#if showError}
            Błąd przy próbie dodawania przedmiotu
        {/if}
        {#if addStatus}
            Pomyślnie dodano przedmiot!
        {/if}
        <h3>Dodaj Przedmiot</h3>
        <form on:submit|preventDefault={addItem}>
            <label>
                <div>Tytuł: </div>
                <input bind:value={title} required>
            </label>
            <label>
                <div>Opis przedmiotu: </div>
                <input bind:value={desc} required>
            </label>
            <label>
                <div>Cena: </div>
                <input bind:value={price} required>
            </label>
            <label>
                <div>Obraz: </div>
                <input type="file" id="image_input" accept="image/png">    
            </label>
            <label>
                <div>Tagi: </div>
                <textarea bind:value={tags[tags]} required></textarea>
            </label>
            <input class="button" type='submit' value='Dodaj'>
        </form>
        <a href="/admin/panel">Powrót do panelu admina</a>   
    </div>
</div>

<style>
    .content{
        display: block;
        margin: auto;
        width: 70%;
        align-items: center;
        justify-content: center;
    }
    .addItem{
        margin: 50px;
        text-align: left;
    }
    .getItems {
        display: block;
        justify-content: left;
        margin: auto;
    }

    label {
        display: block;
    }
    .button {
        margin-bottom: 10px;
        margin-top: 10px;
    }
    textarea {
        width: 40%;
    }
</style>