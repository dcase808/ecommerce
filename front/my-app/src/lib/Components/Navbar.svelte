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
                <input id="search" type="text" bind:value={value}  placeholder="Wpisz frazę do wyszukania" name="search" required>
                <button id="search-button" type="submit">Wyszukaj</button>
            </form>
        </div>
        <a class="link" href="/user">Twoje konto</a>
        <a class="link" href="/cart">Koszyk</a>
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
            background-color: white;
            font-size: 15px;
            color: black;
        }
    </style>