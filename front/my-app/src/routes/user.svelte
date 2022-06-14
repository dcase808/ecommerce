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


    const getOrders = async () => {
        let url = API_URL + '/orders/'
        return await fetch(url, {
        headers: {
            'Authorization': 'Bearer ' + Cookies.get('jwt-token')}
        })
        .then(response => response.json())
		.then(response => response)
		.catch(e => console.error(e))
    } 
               

    let orders = getOrders()
    let user = getUser()

</script>

<main>
    {#if loggedIn}
    <div class="user">
    {#await user}
        Loading
    {:then user} 
       <User id={user._id} name={user.name} address={user.address} postal_code={user.postal_code} city={user.city}/>        
    {/await}
    </div>
    
    {#await orders}
        Loading
    {:then orders}
    <section>
    {#each orders as order }
        <Orders _id={order._id} item = {order.item}  price = {order.price} paid = {order.paid} />
    {/each}
    </section>    
    {/await} 
    {/if}
</main>

<style>
    main {
        margin: auto;
        width: 70%;
        display: flex;
    }
    section {
        width: 70%;
        margin: 20px;
    }
    .user {
        margin: 20px;
    }
</style>
