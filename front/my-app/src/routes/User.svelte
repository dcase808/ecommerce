<script>
    import { goto } from '$app/navigation'; 
    import Cookies from 'js-cookie'
    import { onMount } from 'svelte';
    import {API_URL} from '$lib/Constans/Constans.svelte'
    import User from '../lib/Components/User.svelte';
import Orders from '../lib/Components/Orders.svelte';

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

    const checkIfLoggedIn = async () => {
        if(Cookies.get('jwt-token'))
        {
            validateAndForward()
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

    const getUser = async () => {
        if(Cookies.get('jwt-token')) {
            validateAndForward()
            let url = API_URL + '/users/me'
		    return await fetch(url)
		    .then(response => response.json())
		    .then(response => response)
            .catch(e => console.error(e))
        }
    }

    const getOrders = async () => {
        if(Cookies.get('jwt-token')) {
            validateAndForward()
            let url = API_URL + '/orders/'
		    return fetch(url)
		    .then(response => response.json())
		    .then(response => response)
            .catch(e => console.error(e))
        }
    }

    let orders = getOrders()
    let user = getUser()
</script>

<div>
    <p>Tu bedzie info o koncie</p>
    {#if loggedIn}
    {#await user}
        Loading
    {:then user} 
       <User id={user._id} name={user.name} address={user.address} postal_code={user.postal_code} city={user.city}/>
    {/await}
    Zamowienia
    
    {#await orders}
        Loading
    {:then orders} 
    <Orders _id={orders._id} item = {[orders.id, orders.quantity]}  price = {orders.price} paid = {orders.paid} /> 
    {/await}
    <button on:click={logout}>Wyloguj</button>   
    {/if}
</div>