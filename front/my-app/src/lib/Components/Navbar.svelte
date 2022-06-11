<script>
    import { goto } from '$app/navigation';
    let value;

    const searchForward = () => {
        goto('/search/' + value)
    }
</script>

    <div class="menu">
        <div class="search-container">
            <form on:submit|preventDefault = {searchForward}>
                <input id="search" type="text" bind:value={value}  placeholder="Wyszukaj..." name="search" required>
                <button id="search-button" type="submit">Wyszukaj</button>
            </form>
        </div>
        <a class="link" href="kontakt">Kontakt</a>
        <a class="link" href="/account">Twoje konto</a>
    </div>

    <style>
        .menu{
            display: flex;
            align-items: center;
            width: 80%;
        }
        .link{
            width: 60%;
            text-align: center;
            font-size: 30px;
            text-decoration: none;
            color: rgb(0, 0, 0);
        }
        .search-container {
            width: 100%;
        }
        .search-container button {
            float: right;
            font-size: 15px;
            border: none;
            cursor: pointer;
            width: 20%;
            height: 30px;
            margin-top: 2px;
        }
        #search{
            width: 75%;
            height: 30px;
            float: center;
            background-color: white;
            color: black;
        }
        #search-button{
            background-color: burlywood;
            border: solid gray 2px;
            font-size: 20px;
            color: black;
            font-weight: bold;
            font-family: 'Courier New', Courier, monospace;
        }
    </style>