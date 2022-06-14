<script>
    import { onMount } from 'svelte';
    import {goto} from '$app/navigation';
    import Cookies from 'js-cookie'
    import {ADMIN_API_URL} from '$lib/Constans/Constans.svelte'

    let id
    let loggedIn = false
    let success = false
    let fail = false

    const validateAndForward = async () => {
        let url = ADMIN_API_URL + '/users/me'
        let response = await fetch(url, {
            headers: {'Authorization': 'Bearer ' + Cookies.get('jwt-token-admin')}
        })

        if(!response.ok){
            Cookies.remove('jwt-token-admin')
            goto('/admin')
        }
        loggedIn = true
    }

    const checkIfLoggedIn = async () => {
        if(Cookies.get('jwt-token-admin'))
        {
            validateAndForward()
        }
        else
        {
            goto('/admin')
        }
    }
    onMount(() => {
        checkIfLoggedIn()
    })

    const logout = () => {
        Cookies.remove('jwt-token-admin')
        goto('/')
    }

    const setToPaid = async () => {
        let url = ADMIN_API_URL + '/orders/'
        let body = {
            _id: id,
            paid: true
        }
        let response = await fetch(url, {
            method: "PATCH",
            headers: {'Authorization': 'Bearer ' + Cookies.get('jwt-token-admin'),
            'Content-type': 'application/json'
        },
        body : JSON.stringify(body)
        })
        if(response.ok) {
            success = true   
        }
        else {
            fail = true
        }
    }
</script>

<main>
    {#if loggedIn}
        <a href="/admin/addItem">Dodaj przedmiot</a> <br>
        {#if success}
            <span>
                Zmieniono status zamówienia na opłacone!
            </span>
        {/if}
        {#if fail}
            <span>
                Błąd w zmianie statusu zamówienia.
            </span>
        {/if}
        <input type="text" bind:value={id} placeholder="id zamówienia">
        <button on:click={setToPaid}>Zmień na opłacone</button>
        <button on:click={logout}>Wyloguj</button>
    {/if}    
</main>

<style>
    main {
        padding: 20px;
        align-items: center;
        display: flex;
    }
    button {
        display: flex;
        margin: 30px;
    } 
    a {
        display: flex;
        margin: 30px;
    }
</style>
