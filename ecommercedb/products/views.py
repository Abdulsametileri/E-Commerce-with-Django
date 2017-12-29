from django.http import HttpResponse
from django.shortcuts import render,redirect, render_to_response
from django.views import View
from django.core.urlresolvers import resolve
import datetime
from django.utils import formats

from ecommercedb.views import HomeView
from .models import *
from django.contrib import messages

class SubCategories: # Sabitlerimiz. DB de belirlenmişti. Sub_cat tablosunda.
    Desktop, Laptop, Tablet, Microphone, Gaming_Headphones, Phone_Headsets, Bluetooth, Broom, Iron, Television = range(1,11)


#business logic.

def categoryDispatcher(request):

    current_url = resolve(request.path_info).url_name

    products = None

    if current_url == "desktop":
        products = Product.getBySubCatId(SubCategories.Desktop)
    elif current_url == "laptop":
        products = Product.getBySubCatId(SubCategories.Laptop)
    elif current_url == "tablet":
        products = Product.getBySubCatId(SubCategories.Tablet)
    elif current_url == "microphone":
        products = Product.getBySubCatId(SubCategories.Microphone)
    elif current_url == "gaming-headphones":
        products = Product.getBySubCatId(SubCategories.Gaming_Headphones)
    elif current_url == "phone-headsets":
        products = Product.getBySubCatId(SubCategories.Phone_Headsets)
    elif current_url == "bluetooth":
        products = Product.getBySubCatId(SubCategories.Bluetooth)
    elif current_url == "broom":
        products = Product.getBySubCatId(SubCategories.Broom)
    elif current_url == "iron":
        products = Product.getBySubCatId(SubCategories.Iron)
    elif current_url == "television":
        products = Product.getBySubCatId(SubCategories.Television)

    numrows = len(products)
    product_list = []
    for row in range(0, numrows):
        product = {
            'name': products[row][1],
            'description': products[row][2],
            'url': products[row][3],
            'viewed': products[row][4],
            'price': products[row][5],
            'stock': products[row][6],
            'id': products[row][7]
        }
        product_list.append(product)

    email = request.session.get('email')

    return render_to_response('./products/product.html', {'product_list': product_list, 'email':email})

def productDetail(request,id):

    prod = Product.getById(id)
    prodAttr = Product.getAttrById(id)

    numrows = len(prodAttr)
    product = {
        'Name': prod[0],
        'Description': prod[1],
        'url': prod[2],
        'Viewed': prod[3],
        'Price': prod[4],
        'Stock': prod[5]
    }

    # teknik özellikleri dinamik olarak çekiyor.
    for i in range(0, numrows):
        attribute_name = prodAttr[i][0]
        attribute_value = prodAttr[i][1]
        value = attribute_value
        product[attribute_name] = value

    product_list = getTopThreeRandomProduct();


    return render(request, "./products/product_detail.html", {'product': product, 'product_list':product_list})

class OrderView(View):

    def get(self, request, id):

        prod = Product.getById(id)
        product = {
            'name': prod[0],
            'price': prod[4],
            'stock': prod[5]
        }

        email = request.session.get('email')
        # loginde veya registerde set edilen değeri, get ediyoruz.
        # session pythonda globaller için kullanılıyor.

        product_list = getTopThreeRandomProduct()

        return render(request, "./products/order.html", {'product': product, 'email': email, 'product_id':id, 'product_list':product_list})

    def post(self, request, id):
        params = request.POST

        email = request.session.get('email')

        now = datetime.datetime.now()
        given_date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)

        order_details = {
            'fname': params['first_name'],
            'lname': params['last_name'],
            'address': params['address'],
            'phone': params['phone'],
            'card_name': params['card_name'],
            'card_number': params['card_number'],
            'card_cvc': params['card_cvc'],
            'email': email,
            'piece': params['amount'],
            'carg_name': params['dropdown'],
            'given_date': given_date,
            'product_id': id
        }

        stock_no = Product.checkStock(id)
        if stock_no > int(params['amount']):
            op_result = Product.giveOrder(None, order_details)
            if op_result > 0:
                messages.success(request, 'Your order was taken! Thanks')
            else:
                messages.error(request, "We are encountered an error!")
            return redirect("home")
        else:
            return HttpResponse("There is no enough stock as you want.")






def getTopThreeRandomProduct():
    products = Product.getTopThreeRandomProduct()

    numrows = len(products)
    product_list = []
    for row in range(0, numrows):
        product = {
            'name': products[row][1],
            'description': products[row][2],
            'url': products[row][3],
            'viewed': products[row][4],
            'price': products[row][5],
            'stock': products[row][6],
            'id': products[row][7]
        }
        product_list.append(product)


    return product_list











