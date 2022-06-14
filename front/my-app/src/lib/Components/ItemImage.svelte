<script>
    import {ADMIN_API_URL} from '$lib/Constans/Constans.svelte'
    import Cookies from 'js-cookie'
    let addStatus = false;
    let showError = false;
    let image
    let input

    const uploadImage = async () => {
        const file = input.files[0];
        let url = ADMIN_API_URL + '/items/image'
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

        const reader = new FileReader()
        reader.addEventListener("load",function() {
            image.setAttribute("src", reader.result)
        });
        reader.readAsDataURL(file)

        return;
    }

    image = uploadImage()

</script>
<div class="addImage">
    {#if showError}
        Błąd przy dodawania zdjęcia
    {/if}
    {#if addStatus}
        Pomyślnie dodano zdjęcie!
    {/if}
{#await image}
    Loading
{:then image}
    <input
    bind:this={input}
    on:change={image}
    type = "file"
    />
{/await}
</div>