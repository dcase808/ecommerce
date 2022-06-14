<script>
    import {goto} from '$app/navigation';
    import Cookies from 'js-cookie'
    import {ADMIN_API_URL} from '$lib/Constans/Constans.svelte'

    let username, password, showError

    const validateAndForward = async () => {
        let url = ADMIN_API_URL + '/users/me'
        let response = await fetch (url, {
            headers: {'Authorization': 'Bearer ' + Cookies.get('jwt-token-admin')}
        })

        if(response.ok) {
            goto('/admin/panel')
        }
        else {
            Cookies.remove('jwt-token-admin')
        }
    }


    const submit = async () => {
        if(Cookies.get('jwt-token-admin')) {
            validateAndForward()
        }
        else {
            let data = new URLSearchParams()
            data.append('username', username)
            data.append('password', password)
            let url = ADMIN_API_URL + '/users/token'
            console.log(url)
            let response = await fetch(url, {
                method: 'POST',
                headers: {'Content-type': 'application/x-www-form-urlencoded'},
                body: data
            })
                
            if(response.ok) {
                let body = await response.json()
                showError = false;
                Cookies.set('jwt-token-admin', body.access_token, {sameSite: 'strict'})
                validateAndForward()
                }
            else {
                showError = true
            }
        }
    }

    if(Cookies.get('jwt-token-admin'))
    {
        validateAndForward()
    }
</script>

<div id="content">
    <div id="login">
        {#if showError}
            Błędny login lub hasło
        {/if}
        <form on:submit|preventDefault={submit}>
            <label><br><br><br>
                <span>Podaj login</span><br>
                <input type='text' bind:value={username} required><br><br>   
            </label>
            <label>
                <span>Wpisz hasło:</span><br>
                <input type='password' bind:value={password} required><br><br>
            </label><br>
            <input class="buttons" type='submit' value='Zaloguj'>
        </form>
    </div>
</div>
<style>
    #content {
        width: 70%;
        margin: auto;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
</style>