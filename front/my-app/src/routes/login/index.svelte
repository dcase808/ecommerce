<script>
    import {goto} from '$app/navigation';
    import Cookies from 'js-cookie'
    import {API_URL} from '$lib/Constans/Constans.svelte'
    import { onMount } from 'svelte';
import { update_await_block_branch } from 'svelte/internal';

    let username, password;

    let registerUsername;
    let registerPassword;
    let nameAndSecondName; 
    let address;
    let postal_code;
    let city;

    let showError = false;
    let googleLoginError = false
    let showErrorRegister = false;
    let registerStatus = false;

    async function googleRegister(response){
        let token = await registerGoogle(response.credential)
        if(token.detail == "Unauthorized"){
           showErrorRegister = true
        }
        else{
            registerStatus = true
        }
    }

    globalThis.googleLogin = async (response) =>{
        let token = await loginGoogle(response.credential)
        if(token.detail == "Unauthorized"){
            googleLoginError = true
        }
        else{
            Cookies.set('jwt-token', token.access_token)
            validateAndForward()
        }
    }

    onMount(() => {
        window.googleRegister = googleRegister
        window.googleLogin = googleLogin
    })

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

    const loginGoogle = async (token) => {
        let url = API_URL + '/users/token/ouath?token=' + token
        return await fetch(url, {
            method: 'POST',
            headers: {'Content-type': 'application/json'},
        })
        .then(response => response.json())
        .then(response => response)
    }
    const registerGoogle = async (token) => {
        let url = API_URL + '/users/register/ouath?token=' + token
        return await fetch(url, {
            method: 'POST',
            headers: {'Content-type': 'application/json'},
        })
        .then(response => response.json())
        .then(response => response)
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
<svelte:head>
    <script src="https://accounts.google.com/gsi/client" async defer></script>
</svelte:head>

<div id="content">
    <div id="login">
        {#if showError}
            Błędny login lub hasło
        {/if}
        {#if googleLoginError}
            Brak konta społecznościowego w bazie
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
            <div id='google-login'>
                <div id="g_id_onload"
                data-client_id="541531122590-o9cokanrj3caf6lhhrfen97v604b1896.apps.googleusercontent.com"
                data-callback="googleLogin"
                data-auto_prompt="false">
            </div>
            <div class="g_id_signin"
                data-type="icon"
                data-size="medium"
                data-theme="outline"
                data-text="sign_in_with"
                data-shape="rectangular"
                data-logo_alignment="left">
            </div>
            </div>
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
            <input class="buttons" type='submit' value='Zarejestruj'>

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
    #google-login{
        float: right;
    }
    #google-register{
        float: left;
    }
    .buttons{
        width: 200px;
        height: 32px;
        border: none;
    }
</style>
