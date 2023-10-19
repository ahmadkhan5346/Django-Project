
// #36 video about session storage and local storage
// Find out the cart items from localstorage
if (localStorage.getItem('cart') == null) {
    var cart = {};
}

else {
    cart = JSON.parse(localStorage.getItem('cart'));
    // document.getElementById('cart').innerHTML = Object.keys(cart).length;
    updateCart(cart);
}


// if add to cart button is clicked, add/increment the item
// $('.cart').click(function () {
$('.divpr').on('click', 'button.cart', function () {
    var idstr = this.id.toString();
    console.log('idstr',idstr)
    
    if (cart[idstr] != undefined) {
        qty = cart[idstr][0] + 1;
        console.log('undefined', qty)
    }

    else {
        qty = 1;
        name = document.getElementById('name'+idstr).innerHTML;
        price = document.getElementById('price'+idstr).innerHTML;
        cart[idstr] = [qty, name, parseInt(price)];
        console.log('cart', cart);
    }

    updateCart(cart);

});

// Add popover to cart. add the html in cart in basic.html
$('#popcart').popover();
// document.getElementById('popcart').setAttribute('data-content', '<h5>Cart for Your items in my shopping cart</h5>');

updatePopover(cart);
function updatePopover(cart) {
    var popStr = "";
    popStr = popStr + "<h5>Cart for Your items in my shopping cartt</h5><div class='mx-2 my-2'>";

    var i = 1;
    for (var item in cart) {
        popStr = popStr + "<b>" + i + "</b>. ";
        popStr = popStr + document.getElementById('name' + item).innerHTML.slice(0, 20) + "...Qty: " + cart[item][0] + '<br>';
        i = i + 1;
    }
    popStr = popStr + "</div> <a href='/shop/checkout'><button class='btn btn-primary' id='checkout'>Checkout</button></a> <button class='btn btn-primary' onclick='clearCart()' id='clearCart'>Clear Cart</button>"
    document.getElementById('popcart').setAttribute('data-content', popStr);
    $('#popcart').popover('show');
}


function clearCart() {
    cart = JSON.parse(localStorage.getItem('cart'));
    for (var item in cart) {
        document.getElementById('div' + item).innerHTML = '<button id="' + item + '" class="btn btn-primary cart">Add To Cart</button>';
    }
    localStorage.clear();
    cart = {};
    updateCart(cart);
}


function updateCart(cart) {
    var sum = 0
    for (var item in cart) {  //item = pr1, pr2 etc
        sum = sum + cart[item][0]
        document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''> " + cart[item][0] + " </span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = sum;
    updatePopover(cart);
}

// If plus or minus button is clicked, change the cart as well as the display value #44 video
$('.divpr').on("click", "button.minus", function () {
    a = this.id.slice(7,);
    cart['pr' + a][0] = cart['pr' + a][0] - 1;
    cart['pr' + a][0] = Math.max(0, cart['pr' + a][0]);
    // document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    if (cart['pr' + a][0] == 0){
        document.getElementById('divpr' + a).innerHTML = '<button id="pr'+a+'" class="btn btn-primary cart">Add to Cart</button>';
        delete cart['pr' + a];
    }
    else{
        document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    }
    updateCart(cart);
});

$('.divpr').on("click", "button.plus", function () {
    a = this.id.slice(6,);
    cart['pr' + a][0] = cart['pr' + a][0] + 1;
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    updateCart(cart);
});