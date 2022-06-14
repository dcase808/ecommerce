<script>
import '../app.css';
import Header from '../lib/Components/Header.svelte';
import Footer from '../lib/Components/Footer.svelte';
</script>

<Header/>

<main>
	<slot />
</main>

<Footer/>

<style>
	main {
		flex: 1;
		display: flex;
		width: 100%;
		margin: 0;
		padding: 0;
	}
</style>
