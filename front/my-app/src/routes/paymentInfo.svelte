<script>
    import {page} from '$app/stores';

    let status;

    let url_param = $page.url.searchParams.toString()
    if (url_param == 'error=501') {
        status = false
    }
</script>

<div class="info">
    {#if status}
    Pomyślnie wykonano płatność!
    {:else}
    Błąd przy wykonywaniu płatności.
    {/if}
    <br>
    Sprawdź status zamówienia w zakładce Twoje konto
</div>

<style>
    .info {
        text-align: center;
        margin: auto;
        padding: 20px;
    }
</style>