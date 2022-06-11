<script>
import Navbar from "../Components/Navbar.svelte";

</script>

<header>
	<div class="corner">
		<div id = "logo"> <a href="/"> <img class="logo" src="assets/Drop Shop-logos_black.png" alt="logo"> </a></div>
	</div>

	<Navbar />
</header>

<style>
	header {
		display: flex;
		justify-content: space-between;
		width: 100%;
	}
	.corner{
		width: 20%;
	}
	header{
		background-color: bisque;
	}

	.corner img {
        width: 100%; 
	}


	a:hover {
		color: var(--accent-color);
	}
</style>
