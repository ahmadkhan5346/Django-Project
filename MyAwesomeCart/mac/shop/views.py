from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil

# Create your views here.
# a=<QuerySet [{'category': 'Cleaner', 'id': 2}, {'category': 'Footware', 'id': 3}, {'category': 'Electronics', 'id': 4}]>


def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # n_slides = n//4 + ceil(n/4 - n//4)
    # params = {'no_of_slides': n_slides, 'range': range(1,n_slides), 'product': products}
    
    # all_products = [[products, range(1, n_slides), n_slides],
    #                 [products, range(1, n_slides), n_slides]]

    all_products = []
    category_products = Product.objects.values('category')
    
    category = {item['category'] for item in category_products}
    for cat in category:
        products = Product.objects.filter(category=cat)
        n = len(products)
        n_slides = n//4 + ceil(n/4 - n//4)

        all_products.append([products, range(1, n_slides,), n_slides])
    params = {'allProducts': all_products}
    
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, productid):
    product = Product.objects.get(id=productid)
    return render(request, 'shop/product_view.html', {'product':product})


def checkout(request):
    return render(request, 'shop/checkout.html')
