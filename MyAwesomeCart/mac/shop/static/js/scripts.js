

// Find out the cart items from localstorage
if (localStorage.getItem('cart') == null) {
    var cart = {};
}

else {
    cart = JSON.parse(localStorage.getItem('cart'));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
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

    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;

});

// Add popover to cart. add the html in cart in basic.html
$('#popcart').popover();
document.getElementById('popcart').setAttribute('data-content', '<h5>Cart for Your items in my shopping cart</h5>')

function updateCart(cart) {
    for (var item in cart) {
        document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''> " + cart[item] + " </span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
    }
}

// If plus or minus button is clicked, change the cart as well as the display value