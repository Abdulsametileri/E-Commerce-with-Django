from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views import View
from products.models import Product
from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


class HomeView(View):
    def get(self, request, *args, **kwargs):

        products = Product.getRandomProducts(None)

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

        return render_to_response('./products/product.html', {'product_list': product_list, 'email': email})


