<script>
    import { onMount } from 'svelte';
    import {goto} from '$app/navigation';
    import Cookies from 'js-cookie'
    import {ADMIN_API_URL} from '$lib/Constans/Constans.svelte'

    let loggedIn = false

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
</script>
