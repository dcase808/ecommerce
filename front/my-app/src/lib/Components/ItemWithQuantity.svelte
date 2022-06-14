<script>
    export let id, title, price, img, desc, quantity
</script>
<a href='/items/{id}'>
    <section>
        <div class='img_wrapper'>
            <img src={img} alt={title + ' img'} class='img'>
        </div>
        <div class='summary'>
            <div class='title'>{title}</div>
            <div class='price'>{price.toFixed(2)} PLN</div>
            <div class='desc'>{desc}</div>
        </div>
        <div class='quantity'>
            Sztuk: {quantity}<br>
            Suma częściowa:<br>
            {(quantity * price).toFixed(2)} PLN
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
        align-items: center;
        justify-content: space-around;
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
    .quantity {
        float: right;
        text-align: right;
        margin-left: auto;
        margin-right: 20px;
        width: 20%;
    }
</style>