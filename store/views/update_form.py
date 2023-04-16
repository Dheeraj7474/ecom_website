from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order


class UpdateFormView(View):
     def post(self , request ):
            product = request.POST.get("product")
            ids = []
            ids.append(product)
            products = Products.get_products_by_id(ids)
            return render(request , 'update_form.html',{'products' : products})
