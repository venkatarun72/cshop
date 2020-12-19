from django.views import View
from django.shortcuts import redirect
from store.models.product import Product
from store.models.customer import Customer
from store.models.Orders import Order

class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(customer, address, phone, products, cart, products)

        for product in products:
            order = Order(customer=Customer(id=customer), product=product,
                          price=product.price, quantity=cart.get(str(product.id)), address=address,
                          phone=phone)
            order.placeOrder()
        request.session['cart'] = {}
        return redirect('cart')
