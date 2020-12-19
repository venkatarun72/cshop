from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        customer = Customer(first_name=first_name, last_name=last_name,
                            phone=phone, email=email, password=password)
        error_msg = self.validatecustomer(customer)

        if not error_msg:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_msg,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validatecustomer(self, customer):
        error_msg = None
        if not customer.first_name:
            error_msg = "First Name is required"
        elif len(customer.first_name) < 4:
            error_msg = "First Name must be 4 chars"
        elif not customer.last_name:
            error_msg = "Last Name is required"
        elif len(customer.last_name) < 4:
            error_msg = "Last name is must be 4 chars"
        elif not customer.phone:
            error_msg = "Phone number is required"
        elif len(customer.phone) < 10:
            error_msg = "Phone Number must be 10 digits"
        elif not customer.email:
            error_msg = "Email is required"
        elif len(customer.email) < 5:
            error_msg = "Email must 5 chars long"
        elif not customer.password:
            error_msg = "Password is required"
        elif len(customer.password) < 6:
            error_msg = "Password is must 6 chars"
        elif customer.is_Exists():
            error_msg = "Email already registered"
        return error_msg
