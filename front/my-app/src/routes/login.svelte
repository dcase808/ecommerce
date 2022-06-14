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
        else {
            Cookies.remove('jwt-token')
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
            <div class='form-text'>Zaloguj</div>
            <label>
                <div>E-mail:</div>
                <input type='text' bind:value={username} required>
            </label>
            <label>
                <div>Hasło:</div>
                <input type='password' bind:value={password} required>
            </label>
            <input class="buttons" type='submit' value='Zaloguj'>
        </form>
    </div>

    <div id="register">
        {#if showErrorRegister}
            Błąd przy próbie rejestracji
        {/if}
        {#if registerStatus}
            Pomyslnie zarejestrowano konto!
        {/if}
        <form on:submit|preventDefault={registerSubmit}>
            <div class='form-text'>Zarejestruj</div>
            <label>
                <div>E-mail:</div>
                <input type='email' bind:value={registerUsername} required>
            </label>
            <label>
                <div>Imie i nazwisko:</div>
                <input type='text' bind:value={nameAndSecondName} required>
            </label>
            <label>
                <div>Kod pocztowy</div>
                <input type='text' bind:value={postal_code} required>
            </label>
            <label>
                <div>Adres:</div>
                <input type='text' bind:value={address} required>
            </label>
            <label>
                <div>Miasto:</div>
                <input type='text' bind:value={city} required>
            </label>
            <label>
                <div>Hasło</div>
                <input type='password' bind:value={registerPassword}  required>
            </label>
            <input class="buttons" type='submit' value='Zarejestruj się'>
        </form>
    </div>
</div>
<style>
    #content{
        display: flex;
        margin: auto;
        width: 70%;
        align-items: center;
        justify-content: center;
    }
    #login {
        margin: 50px;
        text-align: right;
    }
    #register {
        margin: 50px;
    }
    label {
        display: block;
    }
    .form-text {
        font-weight: bold;
        margin-bottom: 5px;
        text-align: center;
    }
</style>
