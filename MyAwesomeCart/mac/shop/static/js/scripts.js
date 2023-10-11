
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

    if (cart[idstr] != undefined) {
        cart[idstr] = cart[idstr] + 1;
    }

    else {
        cart[idstr] = 1;
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
        popStr = popStr + document.getElementById('name' + item).innerHTML.slice(0, 20) + "...Qty: " + cart[item] + '<br>';
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
    for (var item in cart) {
        console.log(item)
        sum = sum + cart[item]
        document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''> " + cart[item] + " </span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = sum;
    updatePopover(cart);
}

// If plus or minus button is clicked, change the cart as well as the display value #44 video
$('.divpr').on("click", "button.minus", function () {
    a = this.id.slice(7,);
    cart['pr' + a] = cart['pr' + a] - 1;
    cart['pr' + a] = Math.max(0, cart['pr' + a]);
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a];
    updateCart(cart);
});

$('.divpr').on("click", "button.plus", function () {
    a = this.id.slice(6,);
    cart['pr' + a] = cart['pr' + a] + 1;
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a];
    updateCart(cart);
});