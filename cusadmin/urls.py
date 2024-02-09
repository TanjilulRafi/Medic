from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('admindash',views.admindash,name="admindash"),
    path('adminlogout',views.adminlogout,name="adminlogout"),
    path('adminproduct',views.adminproduct,name="adminproduct"),
    path('admincomplain',views.admincomplain,name="admincomplain"),
    path('admincomplain/<contact_id>',views.deletecom,name="deletecom"),
    path('editprod/<product_id>',views.editprod,name="editprod"),
    path('deleteprod/<product_id>',views.deleteprod,name="deleteprod"),
    path('addprod',views.addprod,name="addprod"),
    path('order',views.order,name='order'),
    path('deleteorder/<order_id>',views.deleteorder,name="deleteorder"),
    path('editorder/<order_id>',views.editorder,name="editorder"),
    path('adminsearch',views.adminsearch,name="adminsearch"),
]