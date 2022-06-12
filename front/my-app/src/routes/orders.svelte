<script>
    import { API_URL } from '$lib/Constans/Constans.svelte'
    import Cookies from 'js-cookie'
    import { goto } from '$app/navigation'
    import { onMount } from 'svelte';
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

    const getOrders = async () => {
        if(Cookies.get('jwt-token')) {
            validateAndForward()
            let url = API_URL + '/orders/'
            console.log(url)
		    return fetch(url)
		    .then(response => response.json())
		    .then(response => response)
            .catch(e => console.error(e))
        }
    }
    let orders = getOrders()
</script>

<div>
    {#await orders}
    Loading    
    {:then orders}
    <Orders id={orders._id} item={orders.item}/>  
    {/await}
    </div>
<p>Tu beda zamuwienia</p>