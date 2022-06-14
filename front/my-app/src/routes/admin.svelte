<script>
    import {goto} from '$app/navigation';
    import Cookies from 'js-cookie'
    import {API_URL} from '$lib/Constans/Constans.svelte'

    let username, password;

    let registerUsername;
    let registerPassword;
    let nameAndSecondName; 
    let address;
    let postal_code;
    let city;

    let showError = false;
    let showErrorRegister = false;
    let registerStatus = false;

    const validateAndForward = async () => {
        let url = API_URL + '/users/me'
        let response = await fetch (url, {
            headers: {'Authorization': 'Bearer ' + Cookies.get('jwt-token')}
        })

        if(response.ok) {
            goto('/user')
        }
    }


    const submit = async () => {
        if(Cookies.get('jwt-token')) {
            validateAndForward()
        }
        else {
            let data = new URLSearchParams()
            data.append('username', username)
            data.append('password', password)
            let url = API_URL + '/users/token'
            console.log(url)
            let response = await fetch(url, {
                method: 'POST',
                headers: {'Content-type': 'application/x-www-form-urlencoded'},
                body: data
            })
                
            if(response.ok) {
                let body = await response.json()
                showError = false;
                Cookies.set('jwt-token', body.access_token, {sameSite: 'strict'})
                validateAndForward()
                }
            else {
                showError = true
            }
        }
    }

    const registerSubmit = async () => {

        if(Cookies.get('jwt-token')) {
            validateAndForward()
        }
        else {

            let data = {
                _id: registerUsername,
                name: nameAndSecondName,
                address: address,
                postal_code: postal_code,
                city: city,
                password: registerPassword
            }
            let url = API_URL + '/users/register'           
            let response = await fetch(url, {
                method: 'POST',
                headers: {'Content-type': 'application/json'},
                body: JSON.stringify(data)
            })
                
            if(response.ok) {
                showErrorRegister = false;
                registerStatus = true;
                }
            else {
                showErrorRegister = true
            }
        }
    }

    if(Cookies.get('jwt-token'))
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
                <span>Podaj email:</span><br>
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
