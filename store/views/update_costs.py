from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order


class UpdateCostsView(View):
    def post(self , request ):
            product_id = request.POST.get("product")
            ids = []
            ids.append(product_id)
            products = Products.get_products_by_id(ids)
            main_product = Products()
            for product in products:
                  main_product = product
            main_product.revenue = float(request.POST.get("revenue"))
            print(main_product.revenue)
            main_product.cogs = float(request.POST.get("costOfGoodsSold"))
            main_product.op_exp = float(request.POST.get("operatingExpenses"))
            main_product.dep = float(request.POST.get("depreciation"))
            main_product.interest_exp = float(request.POST.get("interestExpense"))
            main_product.taxes = float(request.POST.get("taxes"))
            main_product.price = main_product.revenue-main_product.cogs-main_product.op_exp-main_product.dep-main_product.interest_exp-main_product.taxes
            main_product.save()
            return render(request , 'details.html',{'products':products})
