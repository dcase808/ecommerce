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
            console.log(url)            
            let response = await fetch(url, {
                method: 'POST',
                headers: {'Content-type': 'application/json'},
                body: JSON.stringify(data)
            })
                
            if(response.ok) {
                //let body = await response.json()
                showErrorRegister = false;
                registerStatus = true;
                //Cookies.set('jwt-token', body.access_token, {sameSite: 'strict'})
               // validateAndForward()
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

    <div id="register">
        {#if showErrorRegister}
        Błąd przy próbie rejestracji
        {/if}
        {#if registerStatus}
        Pomyslnie zarejestrowano konto!
        {/if}
        <form on:submit|preventDefault={registerSubmit}>
            <label>
                <span>Podaj email:</span><br>
                <input type='text' bind:value={registerUsername} required><br><br>
            </label>
            <label>
                <span>Podaj imie i nazwisko:</span><br>
                <input type='text' bind:value={nameAndSecondName} required><br><br>
            </label>
            <label>
                <span>Podaj kod pocztowy</span><br>
                <input type='text' bind:value={postal_code} required><br><br>
            </label>
            <label>
                <span>Podaj adres:</span><br>
                <input type='text' bind:value={address} required><br><br>
            </label>
            <label>
            <label>
                <span>Podaj miasto:</span><br>
                <input type='text' bind:value={city} required><br><br>
            </label>
                <span>Podaj hasło</span><br>
                <input type='password' bind:value={registerPassword}  required><br><br>
            </label>
            <input class="buttons" type='submit' value='Zarejestruj się'>
        </form>
    </div>
</div>
<style>
    #login{
        float: right;
        width: 50%;
        text-align: center;
    }

    #register{
        text-align: center;
        width: 50%;
    }

    #content{
        display: flex;
        width: 100%;
        margin: 0;
        padding: 0;
    }

    form{
        padding: 0;
        margin: 0;
    }

    .buttons{
        background-color: burlywood;
            border: solid gray 2px;
            font-size: 20px;
            color: black;
            font-weight: bold;
            font-family: 'Courier New', Courier, monospace;
    }
    span{
        font-size: 25px;
        font-weight: bold;
    }
</style>
