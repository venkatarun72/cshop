from django.contrib.auth.hashers import check_password
from django.views import View
from django.shortcuts import render, redirect
from store.models.customer import Customer


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                return redirect('homepage')
            else:
                error_msg = "Email or Password is invalid"
        else:
            error_msg = "Email or Password is invalid"
        print('You are :', email)
        return render(request, 'login.html', {'error': error_msg})


def logout(request):
    request.session.clear()
    return redirect('login')
