<script>
    import { goto } from '$app/navigation';
    import Cookies from 'js-cookie'
    export let id, name, address, postal_code, city

    const logout = () => {
        Cookies.remove('jwt-token')
        goto('/')
    }
</script>

<div class="user">
    <div class="e-mail">E-mail: {id}</div>
    <div class="name">Imię i nazwisko: {name}</div>
    <div class="address">Adres: {address} <br> {postal_code} {city}</div>
    <button on:click={()=>{goto('user/edit')}}>Edytuj</button>
    <button on:click={logout}>Wyloguj</button>
</div>

<style>
    .user {
        margin: auto;
        width: 70%;
        display: inline;
        margin-top: 20px;
    }

</style>