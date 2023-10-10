
// #36 video about session storage and local storage
// Find out the cart items from localstorage
if (localStorage.getItem('cart') == null) {
    var cart = {};
    console.log('mt dic:', cart)
}

else {
    cart = JSON.parse(localStorage.getItem('cart'));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
    console.log('else:', cart)
    updateCart(cart);
}


// if add to cart button is clicked, add/increment the item
$('.cart').click(function () {
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
document.getElementById('popcart').setAttribute('data-content', '<h5>Cart for Your items in my shopping cart</h5>');

function updateCart(cart) {
    for (var item in cart) {
        document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''> " + cart[item] + " </span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
    console.log(cart)
}

// If plus or minus button is clicked, change the cart as well as the display value #44 video
$('.divpr').on("click", "button.minus", function(){
    a = this.id.slice(7);
    cart['pr' + a] = cart['pr' + a] - 1;
    cart['pr' + a] = Math.max(0, cart['pr' + a]);
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a];
});

$('.divpr').on("click", "button.plus", function(){
    a = this.id.slice(4);
    b = this.id.slice(6);
    cart[a] = cart[a] + 1;
    document.getElementById('valpr' + b).innerHTML = cart[a];
});