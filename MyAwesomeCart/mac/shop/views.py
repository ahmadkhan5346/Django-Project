import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
from django.views.decorators.csrf import csrf_exempt
from paytmchecksum import PaytmChecksum

# pip3 install pycryptodome
Merchant_ID = 'QCuIPX84986814278300'
Merchant_Key = 'fzEAM4mKN67_Os&&'
Website = 'WEBSTAGING'
Industry_Type = 'Retail'
Channel_ID  = 'WEB'               # (For Website)
Channel_ID = 'WAP'                     # (For Mobile Apps)
request_url = 'https://securegw-stage.paytm.in/order/sendpaymentrequest'

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
    thank = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True

    return render(request, 'shop/contact.html', {'thank':thank})


def tracker(request):
    if request.method == "POST":
        order_id = request.POST.get('orderId')
        email = request.POST.get('email')
        try:
            order = Order.objects.filter(order_id=order_id, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp})
                response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, productid):
    product = Product.objects.get(product_id=productid)
    return render(request, 'shop/product_view.html', {'product':product})


def checkout(request):
    if request.method == 'POST':
        item_json = request.POST.get('itemsJson')
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address1') +' '+ request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        order = Order(
            items_json=item_json, amount=amount, name=name, email=email, address=address,
            city=city, state=state, zip_code=zip_code, phone=phone
        )
        # order.save()

        ord_update = OrderUpdate(order_id=order.order_id, update_desc="The Order has been placed")
        # ord_update.save()
        thank = True
        id = order.order_id
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})

        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {
            'MID':Merchant_ID,
            'ORDER_ID':1,
            'TXN_AMOUNT':'1',
            'CUST_ID':order.email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlepayment/'
        }
        # print('parammmmmmmm:', param_dict)
        return render(request, 'shop/paytm.html', {'param_dict':param_dict})
    return render(request, 'shop/checkout.html')


# Paytm Integration payment gateway
# Paytm will send you post request here bypass the csrf and using security checksum 
@csrf_exempt
def handlepayment(request):
    return HttpResponse("done")
