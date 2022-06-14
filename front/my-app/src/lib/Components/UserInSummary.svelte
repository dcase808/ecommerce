<script>
    import { goto } from '$app/navigation';
    import Cookies from 'js-cookie'
    import {API_URL} from '$lib/Constans/Constans.svelte'

    const getUser = async () => {
        let url = API_URL + '/users/me'
		return await fetch(url, {
        headers: {
            'Authorization': 'Bearer ' + Cookies.get('jwt-token')}
        })
        .then(response => response.json())
		.then(response => response)
		.catch(e => console.error(e))
    }
    let user = getUser()
</script>
{#await user}
    <span>Loading</span>
{:then user} 
<div class="user">
    <div class="e-mail">E-mail: {user._id}</div>
    <div class="name">Imię i nazwisko: {user.name}</div>
    <div class="address">Adres: {user.address} <br> {user.postal_code} {user.city}</div>
</div>
{/await}


<style>
    .user {
        margin: auto;
        width: 70%;
        display: inline;
        margin-top: 20px;
    }

</style>