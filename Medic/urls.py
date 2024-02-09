from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('profile',views.profile,name="profile"),
    path('contact',views.contact,name="contact"),
    path('checkout/',views.checkout,name="checkout"),
    path("search",views.search,name="search"),
    path('productview/<product_id>',views.productview,name="productview"),
]
