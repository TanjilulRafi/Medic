from django.shortcuts import render,redirect
from Medic.models import Contact,Product,Orders
from django.contrib import messages
from math import ceil
# Create your views here.
def home(request):
    allprods=[]
    catprods=Product.objects.values('category','product_id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4+ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])
    params={'allprods':allprods}
    return render(request,"index.html",params)

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        myquary=Contact(name=name,email=email,phone=phone,desc=desc)
        myquary.save()
        messages.info(request,"Your message has been sent.We will contact you soon!")
        return render(request,"contact.html")
    return render(request,"contact.html")


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')

    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        city = request.POST.get('city', '')
        phone = request.POST.get('phone', '')
        am = int(amount)
        if am<=70:
            messages.warning(request,"Please select atleast total 70Tk to order")
            return redirect('/')
        elif len(phone)<11:
            messages.error(request,"Please enter a valid phone number")
            return redirect('/')
        else:
            Order = Orders(items_json=items_json,name=name,amount=amount, email=email, address1=address1,city=city,phone=phone)
            Order.save()
            thank = True
            messages.success(request,"Your order has been placed successfully")
            return redirect('/')
        
    return render(request,"checkout.html")

def profile(request):
    currentuser=request.user.username
    items=Orders.objects.filter(email=currentuser)
    context={'items':items}
    return render(request,"profile.html",context)


def search(request):
    query=request.GET["getdata"]
    allPostN=Product.objects.filter(product_name__icontains=query)
    allPostG=Product.objects.filter(generic__icontains=query)
    allPosts=allPostN.union(allPostG)
    return render(request,"search.html",{"allPostN":allPostN,"allPostG":allPostG,"allPosts":allPosts})

def productview(request,product_id):
    query=Product.objects.get(product_id=product_id)
    return render(request,"view.html",{'query':query})
