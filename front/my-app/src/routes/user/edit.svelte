<script>
    import {API_URL} from '$lib/Constans/Constans.svelte'
    import Cookies from 'js-cookie'
    import {goto} from '$app/navigation';
    let nameAndSecondName, postal_code, address, city

    const patchUser = async () => {
       let body = {
         name: nameAndSecondName,
         address: address,
         postal_code: postal_code,
         city: city
       }
       let url = API_URL + '/users/me'
       await fetch(url, {
        method:'PUT',
        headers: {'Authorization': 'Bearer ' + Cookies.get('jwt-token'),
        'Content-type': 'application/json'
        },
        body: JSON.stringify(body)
       })
       goto('/user')
    }
</script>

<div class="edit">
    <form on:submit|preventDefault={patchUser}>
        <div class='form-text'>Edytuj Dane</div><br>
        <label>
            <div>Imie i nazwisko:</div>
            <input type='text' bind:value={nameAndSecondName} required>
        </label>
        <label>
            <div>Kod pocztowy</div>
            <input type='text' bind:value={postal_code} required>
        </label>
        <label>
            <div>Adres:</div>
            <input type='text' bind:value={address} required>
        </label>
        <label>
            <div>Miasto:</div>
            <input type='text' bind:value={city} required><br>
        </label>
        <input class="buttons" type='submit' value='Edytuj'>

    </form>
</div>

<style>
    .edit{
        width: 100%;
        margin: 20px;
        text-align: center;
    }
</style>
