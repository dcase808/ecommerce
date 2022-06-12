<script>
    import { goto } from '$app/navigation'; 
    import Cookies from 'js-cookie'
    import { onMount } from 'svelte';
    import {API_URL} from '$lib/Constans/Constans.svelte'

    let loggedIn = false


    const validateAndForward = async () => {
        let url = API_URL + '/users/me'
        let response = await fetch(url, {
            headers: {'Authorization': 'Bearer ' + Cookies.get('jwt-token')}
        })

        if(!response.ok){
            Cookies.remove('jwt-token')
            goto('/Login')
        }
        loggedIn = true
    }

    const getUser = async () => {
        if(Cookies.get('jwt-token')) {
            validateAndForward()
        }
        else {
        return await response.json();
        }
        
    } 
    const users = getUser();

    const checkIfLoggedIn = async () => {
        if(Cookies.get('jwt-token'))
        {
            getUser()
        }
        else
        {
            goto('/Login')
        }
    }
    onMount(() => {
        checkIfLoggedIn()
    })
    const logout = () => {
        Cookies.remove('jwt-token')
        goto('/')
    }
</script>

<div>
    <p>Tu bedzie info o koncie</p>
    {#if loggedIn}
    {#await users}
        loading
    {:then users } 
        <p>{users.name}</p>
        {console.log(users)}
    {/await}
    <button on:click={logout}>Wyloguj</button>
    {/if}
</div>