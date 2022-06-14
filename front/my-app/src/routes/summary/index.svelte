<script>
    import { shopping_cart } from '$lib/stores.js'
    import ItemInCart from '$lib/Components/ItemInCart.svelte';
    import UserInSummary from '$lib/Components/UserInSummary.svelte';
    import { onMount } from 'svelte';
    import {goto} from '$app/navigation';
    import Cookies from 'js-cookie'
    import {API_URL} from '$lib/Constans/Constans.svelte'
        

    const finalize = async () => {
        let order = await createOrder()
        let payment = await createPayment(order._id)
        console.log(payment.redirectUri)
        window.location.href = payment.redirectUri
    }

    const createPayment = async (id) => {
        let url = API_URL + '/payments?order_id=' + id 
        return await fetch(url, {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + Cookies.get('jwt-token'),
                'Content-Type': 'application/json'
                },
        })
        .then(response => response.json())
        .then(response => response)
    }

    const createOrder = async () => {
        let body = {
            item: []
        }
        for (const item of $shopping_cart)
        {
            console.log(item)
            let item_in_json = {
                id: item.item_id,
                quantity: item.quantity
            }
            body.item.push(item_in_json)
        }
        console.log(body)
        let url = API_URL + '/orders'
        return await fetch(url, {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + Cookies.get('jwt-token'),
                'Content-Type': 'application/json'
                },
            body: JSON.stringify(body)
        })
        .then(response => response.json())
        .then(response => response)
    }

    const validateAndForward = async () => {
        let url = API_URL + '/users/me'
        let response = await fetch (url, {
            headers: {'Authorization': 'Bearer ' + Cookies.get('jwt-token')}
        })
        if(!response.ok) {
            goto('/user')
            Cookies.remove('jwt-token')
        }
    }
    const checkIfLoggedIn = async () => {
        if(Cookies.get('jwt-token'))
        {
            validateAndForward()
        }
        else
        {
            goto('/login')
        }
    }

    $: calculateSum = () => {
        let sum = 0
        for (const obj of $shopping_cart)
        {
            sum = sum + obj.quantity * obj.price
        }
        return sum
    }
    const checkIfCartEmpty = () => {
        if ($shopping_cart.length < 1)
        {
            goto('/')
            return true
        }
    }

    onMount(() => {

        if(checkIfCartEmpty())
        {
            goto('/')
        }
        else{
            checkIfLoggedIn()
        }
        
    })
</script>

<main>
    {#each $shopping_cart as item}
    <section>
        <div class='item'>
            <ItemInCart id={item.item_id} quantity={item.quantity}/>
        </div>
    </section>
    {/each}
    <div class='summary-wrapper'>
        <div class='user'>
            <UserInSummary/>
        </div>
        <div class='summary'>Suma: {calculateSum().toFixed(2)} PLN <button class='go-to-payment' on:click={finalize} >Złóż zamówienie</button></div>
    </div>
</main>
<style>
    main{
        width: 70%;
        margin: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .summary-wrapper{
        display: flex;
        width: 100%;
        margin: 20px
    }
    .user{
        margin-right: auto;
        margin-left: 50px;
    }
    section {
        width: 100%;
        display: flex;
        align-items: center;
    }
    .item{
        width: 100%;
    }
    .go-to-payment {
        border: none;
        height: 50px;
        width: 150px;
    }
    .summary {
        margin-left: auto;
        margin: 20px 0px 20px auto;
    }
</style>