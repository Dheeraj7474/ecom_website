from django.contrib import admin
from django.urls import include, path
from django.urls import re_path

from store.views.update_costs import UpdateCostsView
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.details import DetailsView
from .views.update_form import UpdateFormView
from .views.update_costs import UpdateCostsView
from .views.views import MessageHandler


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('details', auth_middleware(DetailsView.as_view()), name='details'),
    path('update-form',UpdateFormView.as_view(),name='updateform'),
    path('update-costs',UpdateCostsView.as_view(),name='updatecosts'),
    path('twilio',MessageHandler.register, name='twilio'),
    path('enter-otp',MessageHandler.enter_otp,name='enter-otp'),
    path('verify-otp',MessageHandler.verify_otp,name='verify-otp')

]
