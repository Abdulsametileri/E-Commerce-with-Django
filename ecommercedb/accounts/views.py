from django.shortcuts import render, redirect, Http404
from django.views import View
from .models import Accounts
from django.contrib.auth import logout
from django.contrib import messages
from products.views import getTopThreeRandomProduct

class RegisterView(View):

    def get(self, request):
        product_list = getTopThreeRandomProduct()

        if request.user.is_authenticated():
            return Http404()
        return render(request, "./accounts/signup_form.html", {'product_list':product_list})

    def post(self, request):
        params = request.POST
        if params['customer_email'] and \
           params['customer_password']:  # bu kolonlar database de not null olarak tanımlı.
            result = Accounts.register(params)
            if result > 0:
                messages.success(request, 'You have successfully registered!')
                return redirect("home")
            else:
                messages.error(request, 'Error! Try again.')
                return render(request, "./accounts/signup_form.html", {})
        else:
            messages.error(request, 'Error! Try again.')
            return render(request, "./accounts/signup_form.html", {})


class LoginView(View):

    def get(self, request):
        product_list = getTopThreeRandomProduct()

        if request.user.is_authenticated():
            return Http404()
        return render(request, "./accounts/login.html", {'product_list':product_list})

    def post(self, request):
        params = request.POST

        if params['email'] and params['password']:
            user = Accounts.authentication(params['email'], params['password'],)

            if user == -1: #Sistemde öyle bir kullanıcı kayıtlı değil ise
                messages.error(request, 'No records found!')
                return render(request, "./accounts/login.html", {})
            elif user == 1:
                #messages.success(request, 'You have successfully logged in')
                return redirect('admin-home')
            else:
                #messages.success(request, 'You have successfully logged in')
                request.session['email'] = params['email']
                return redirect('home')

        else:
            messages.error(request, 'Error! Try again.')
            return render(request, "./accounts/login.html", {})


class SignOutView(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'You have successfully logged out')
        return redirect('home')









