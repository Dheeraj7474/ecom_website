from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class DetailsView(View):
    def post(self , request ):
            product = request.POST.get("product")
            ids = []
            ids.append(product)
            products = Products.get_products_by_id(ids)
            return render(request , 'details.html',{'products' : products})
