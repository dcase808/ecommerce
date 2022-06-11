<script>
import '../app.css';
import Header from '../lib/Components/Header.svelte';
</script>

<Header/>

<main>
	<slot />
</main>

<footer>
	<p>Copyrights 2022 Marcin Koczulap | Filip Zimny | Jakub Ziomek</p>
</footer>

<style>
	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		width: 100%;
		max-width: 1024px;
		margin: 0 auto;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 40px;
		background-color: rgb(107, 71, 17);
	}
</style>
