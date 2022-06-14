<script>
    export let id, name, address, postal_code, city

    const logout = () => {
        Cookies.remove('jwt-token')
        goto('/')
    }
</script>

<div class="user">
    <div class="e-mail">E-mail: {id}</div>
    <div class="name">Imię i nazwisko: {name}</div>
    <div class="address">Adres zamieszkania: {address}</div>
    <div class="postalCode">Kod pocztowy: {postal_code}</div>
    <div class="city">Miasto {city}</div>
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