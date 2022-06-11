<script>
import { get_root_for_style, group_outros } from "svelte/internal";
    let value;
</script>

    <div class="menu">
        <div class="search-container">
            <form on:submit|preventDefault = {() => {goto('/search/' + value)}}>
                <input type="text" bind:value={value} placeholder="Wyszukaj..." name="search">
                <button type="submit">Wyszukaj</button>
            </form>
        </div>
        <a class="link" href="kontakt">Kontakt</a>
        <a class="link" href="konto">Twoje konto</a>
    </div>

    <style>
        .menu{
            display: flex;
            align-items: center;
            width: 100%;
        }
        .link{
            width: 60%;
            text-align: center;
            font-size: 30px;
            text-decoration: none;
            color: rgb(0, 0, 0);
        }
        .search-container button {
            float: right;
            padding: 5px 10px;
            font-size: 15px;
            border: none;
            cursor: pointer;
        }
        .search-container {
            display: flex;
            float: center;
            width: 60%;
        }
    </style>