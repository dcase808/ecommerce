<script>
    export let id, title, price, img, desc
</script>
<a href='/items/{id}'>
    <section>
        <div class='img_wrapper'>
            <img src={img} alt={title + ' img'} class='img'>
        </div>
        <div class='summary'>
            <div class='title'>{title}</div>
            <div class='price'>{price} PLN</div>
            <div class='desc'>{desc}</div>
        </div>
    </section>
</a>
<style>
    section{
        width: 100%;
        min-height: 150px;
        margin-top: 10px;
        margin-bottom: 10px;
        padding: 20px;
        display: flex;
        border: dotted 1px;
    }
    .img {
        height: 150px;
    }
    .img_wrapper {
        width: 150px;
        min-width: 150px;
    }
    .title {
        font-weight: bold;
    }
    .summary {
        margin-left: 20px;
    }
</style>