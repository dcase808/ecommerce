<script>
import Navbar from './Navbar.svelte';
</script>

<header>
	<div class="corner">
		<div id = "logo"> <a href="/"> <img class="logo" src="assets/Drop Shop-logos_black.png" alt="logo"> </a></div>
	</div>

	<Navbar />
	<div class="corner">
		<!-- TODO put something else here? github link? -->
	</div>
</header>

<style>
	header {
		display: flex;
		justify-content: space-between;
	}

	.corner img {
        width: 200px;
        padding: 10px 10px 10px 10px;   
	}


	a:hover {
		color: var(--accent-color);
	}
</style>
