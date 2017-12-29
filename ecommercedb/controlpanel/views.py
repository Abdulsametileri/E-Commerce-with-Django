from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from products.views import getTopThreeRandomProduct

def home(request):
    product_list = getTopThreeRandomProduct()
    return render(request, "./controlpanel/main.html",{'product_list':product_list})

def add_product(request):

    product_list = getTopThreeRandomProduct()

    if request.method == 'POST' and request.FILES['myfile']:
        params = request.POST
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        Admin.insertProduct(
            params['product_name'],
            params['product_description'],
            uploaded_file_url,
            params['product_price'],
            params['product_stock'],
            params['subcat'],
        )

        return redirect('admin-home')
    elif request.method == 'GET':
        return render(request,"./controlpanel/addproduct.html",{'product_list':product_list})


