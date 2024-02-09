from django.db import connection
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Medic.models import Contact,Product,Orders

# Create your views here.


def adminlogin(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('pass')
            user = User.objects.filter(username=username)
            if not user.exists():
                messages.warning(request, "User Not Found")
                return render(request, 'adminlogin.html')
            user = authenticate(username=username, password=password)
            if user and user.is_superuser:
                login(request, user)
                messages.success(request, "Login Successfully")
                return redirect('admindash')
            else:
                messages.warning(request, "Invalid Username or Password")
                return render(request, 'adminlogin.html')

        return render(request,'adminlogin.html')

def admindash(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT count(*) FROM Product')
            row = cursor.fetchone()
            product_count = row[0] if row else 0
            cursor.execute('SELECT count(*) FROM Orders')
            row1 = cursor.fetchone()
            order_count = row1[0] if row1 else 0
            cursor.execute('SELECT count(*) FROM Contact')
            row2 = cursor.fetchone()
            user_count = row2[0] if row2 else 0
            return render(request, 'admindash.html', {'pc': product_count, 'oc': order_count, 'uc': user_count})
    except Exception as e:
        print("Error:", str(e))
        return render(request, 'admindash.html')

def adminlogout(request):
    logout(request)
    messages.success(request,"Logout successfully")
    return redirect('/')

def adminproduct(request):
    obs=Product.objects.all()
    return render(request,'adminproduct.html',{'obs':obs})

def admincomplain(request):
    obs=Contact.objects.all()
    return render(request,'admincomplain.html',{'obs':obs})

def deletecom(request,contact_id):
    query=Contact.objects.get(contact_id=contact_id)
    query.delete()
    messages.success(request,"Complain deletd Successfully..")
    return redirect('admincomplain')

def editprod(request,product_id):
    if request.method=="POST":
        product_name=request.POST['product_name']
        category=request.POST['category']
        generic=request.POST['generic']
        price=request.POST['price']
        desc=request.POST['desc']
        image=request.POST['image']
        query=Product.objects.get(product_id=product_id)
        query.product_name=product_name
        query.category=category
        query.generic=generic
        query.price=price
        query.desc=desc
        query.image=image
        query.save()
        messages.success(request,"Product Updated Successfully")
        return redirect('admindash')
    query=Product.objects.get(product_id=product_id)
    return render(request,'editprod.html',{'query':query})

def deleteprod(request,product_id):
    query=Product.objects.get(product_id=product_id)
    query.delete()
    messages.success(request,"Product deletd Successfully..")
    return redirect('adminproduct')

def addprod(request):
    if request.method=="POST":
        product_name=request.POST['product_name']
        category=request.POST['category']
        generic=request.POST['generic']
        price=request.POST['price']
        desc=request.POST['desc']
        image=request.POST['image']
        if Product.objects.filter(product_name=product_name).exists():
            messages.warning(request,"Product already exists")
            return redirect('addprod')
        query=Product(product_name=product_name,category=category,generic=generic,price=price,desc=desc,image=image)
        query.save()
        messages.success(request,"Product Added Successfully")
        return redirect('adminproduct')
    return render(request,'addprod.html')

def order(request):
    obs=Orders.objects.all()
    return render(request,'order.html',{'obs':obs})

def deleteorder(request,order_id):
    query=Orders.objects.get(order_id=order_id)
    query.delete()
    messages.success(request,"Order deleted Successfully..")
    return redirect('order')

def editorder(request,order_id):
    if request.method=="POST":
        amount=request.POST['amount']
        delivered=request.POST['delivered']
        query=Orders.objects.get(order_id=order_id)
        query.amount=amount
        query.delivered=delivered
        query.save()
        messages.success(request,"Order Updated Successfully")
        return redirect('order')
    query=Orders.objects.get(order_id=order_id)
    return render(request,'editorder.html',{'query':query})

def adminsearch(request):
    query=request.GET["getdata"]
    allPostN=Product.objects.filter(product_name__icontains=query)
    allPostG=Product.objects.filter(generic__icontains=query)
    allPosts=allPostN.union(allPostG)
    return render(request,"adminsearch.html",{"allPostN":allPostN,"allPostG":allPostG,"allPosts":allPosts})

