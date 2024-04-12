from django.shortcuts import render,redirect
from manu.models import categorydb,itemdb
from frontend.models import contactdb,userdb,cartdb,wishlistdb,billdb
from django.contrib import messages
from django.core.paginator import Paginator
#mail
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

# Create your views here.
def homep(request):
    cat = categorydb.objects.all()
    data = itemdb.objects.all()
    late = itemdb.objects.all()[::-1][:8]
    return render(request,"home.html",{'cat':cat,'data':data,'late':late})

def store(request):
    if 'username' in request.session:
        item = itemdb.objects.all()
        dataa = wishlistdb.objects.filter(uname=request.session['name'])
        x = 0
        for i in dataa:
            x += 1
        paginator = Paginator(item, 9)
        page_number = request.GET.get('page')
        data = paginator.get_page(page_number)
        return render(request, "shop.html", {'data': data, 'x': x})
    else:
        item = itemdb.objects.all()
        paginator = Paginator(item, 9)
        page_number = request.GET.get('page')
        data = paginator.get_page(page_number)
        return render(request, "shop.html", {'data': data})

def fstore(request,cn):
    if 'username' in request.session:
        item = itemdb.objects.filter(cname=cn)
        dataa = wishlistdb.objects.filter(uname=request.session['name'])
        x = 0
        for i in dataa:
            x += 1
        paginator = Paginator(item, 9)
        page_number = request.GET.get('page')
        data = paginator.get_page(page_number)
        return render(request, "shop.html", {'data': data, 'x': x})
    else:
        item = itemdb.objects.filter(cname=cn)
        paginator = Paginator(item, 9)
        page_number = request.GET.get('page')
        data = paginator.get_page(page_number)
        return render(request, "shop.html", {'data': data})

def itemd(request,itemid):
    if 'username' in request.session:
        item = itemdb.objects.filter(id=itemid)
        dataa = wishlistdb.objects.filter(uname=request.session['name'])
        x = 0
        for i in dataa:
            x += 1
        return render(request, "productd.html", {'item': item, 'x': x})
    else:
        item = itemdb.objects.filter(id=itemid)
        return render(request, "productd.html", {'item': item})

def blog(request):
    dataa = wishlistdb.objects.filter(uname=request.session['name'])
    x = 0
    for i in dataa:
        x += 1
    return render(request,"blog.html",{'x':x})

def about(request):
    dataa = wishlistdb.objects.filter(uname=request.session['name'])
    x = 0
    for i in dataa:
        x += 1
    return render(request,"about.html",{'x':x})

def contact(request):
    dataa = wishlistdb.objects.filter(uname=request.session['name'])
    x = 0
    for i in dataa:
        x += 1
    return render(request,"contact.html",{'x':x})

def csave(request):
    if request.method == "POST":
        nn = request.POST.get('n')
        ee = request.POST.get('e')
        ss = request.POST.get('s')
        me = request.POST.get('m')
    obj = contactdb(name=nn,email=ee,sub=ss,msg=me)
    obj.save()
    messages.success(request, "Successfully Uploaded.!")
    return redirect(contact)

def userlogin(request):
    return render(request,"userlogin.html")

def usave(request):
    if request.method == "POST":
        nn = request.POST.get('n')
        ee = request.POST.get('e')
        pp = request.POST.get('pa')
        ii = request.FILES['im']
        if userdb.objects.filter(email=ee).exists():
            messages.error(request,'email already exists.!')
            return redirect(userlogin)
        else:
            if userdb.objects.filter(name=nn).exists():
                messages.error(request, 'Username already exists.!')
                return redirect(userlogin)
            else:
                obj = userdb(name=nn, email=ee, password=pp, img=ii)
                obj.save()
                subject = 'Welcome to Fashion Store'
                message = (
                    'We re thrilled to have you join the Fashion Store community🎉.This is just a quick note to say thank you for signing up. We re excited to see you start exploring all that Fashion Store has to offer.')
                recipient = ee
                send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                messages.success(request, "Successfully Registered.!")
                return redirect(userlogin)

def ulogin(request):
    if request.method == "POST":
        ee = request.POST.get('n')
        pwd = request.POST.get('pas')
        if userdb.objects.filter(name=ee,password=pwd).exists():
            request.session['name']= ee
            request.session['password']= pwd
            messages.success(request, "Login Successfully.!")
            return redirect(homep)
        else:
            messages.error(request, "Invalid password.!")
            return redirect(userlogin)
    messages.warning(request, "Inavlid Username.!")
    return redirect(userlogin)

def ulogout(request):
    del request.session['name']
    del request.session['password']
    messages.success(request, "Logout Successfully.!")
    return redirect(userlogin)

def savecart(request):
    if request.method == "POST":
        aa = request.POST.get('q')
        bb = request.POST.get('p')
        cc = request.POST.get('un')
        dd = request.POST.get('pn')
        ee = request.POST.get('tp')
    obj = cartdb(uname=cc,pname=dd,qty=aa,price=bb,tprice=ee)
    obj.save()
    messages.success(request, "Saved to cart.!")
    return redirect(store)

def cartpage(request):
    data = cartdb.objects.filter(uname=request.session['name'])
    dataa = wishlistdb.objects.filter(uname=request.session['name'])
    x = 0
    tprice = 0
    for i in data:
        tprice = tprice+i.tprice
    for i in dataa:
        x += 1
    return render(request,"cart.html",{'data':data, 'tprice':tprice,'x':x})

def deletecart(request,did):
    x = cartdb.objects.filter(id=did)
    x.delete()
    return redirect(cartpage)

def checkout(request):
    data = cartdb.objects.filter(uname=request.session['name'])
    dataa = wishlistdb.objects.filter(uname=request.session['name'])
    e = userdb.objects.get(name=request.session['name']).email
    x = 0
    tprice = 0
    for i in data:
        tprice = tprice+i.tprice
    for i in dataa:
        x += 1
    return render(request,"checkout.html",{'data':data,'tprice':tprice,'x':x,'e':e})

def savecheck(request):
    if request.method == "POST":
        aa = request.POST.get('un')
        bb = request.POST.get('em')
        cc = request.POST.get('ad')
        dd = request.POST.get('ci')
        ee = request.POST.get('co')
        ff = request.POST.get('code')
        gg = request.POST.get('tel')
        obj = billdb(uname=aa, email=bb, address=cc,city=dd,country=ee,code=ff,phone=gg)
        obj.save()
        messages.success(request, "Successfully Saved.!")
        return redirect(checkout)

def wishlist(request,itemid):
    xx = list(wishlistdb.objects.all())
    for yy in xx:
        if yy.pid == itemid and yy.uname == request.session['name']:
            return redirect(store)
    else:
        n = itemdb.objects.get(id=itemid).cname
        ina = itemdb.objects.get(id=itemid).iname
        p = itemdb.objects.get(id=itemid).price
        d = itemdb.objects.get(id=itemid).details
        img = itemdb.objects.get(id=itemid).image
        img1 = itemdb.objects.get(id=itemid).image1
        obj = wishlistdb(pid=itemid, cname=n, uname=request.session['name'], iname=ina, price=p, details=d, image=img,
                         image1=img1)
        obj.save()
        return redirect(store)

def wishlistv(request):
    item = wishlistdb.objects.filter(uname=request.session['name'])
    return render(request,"wish.html",{'item':item})

def deletewish(request,itemid):
    x = wishlistdb.objects.filter(id=itemid)
    x.delete()
    return redirect(wishlistv)

def witemdetails(request,itemid):
    item = wishlistdb.objects.filter(id=itemid)
    return render(request,"wproduct.html",{'item':item})

def searchitem(request):
    if 'username' in request.session:
        dataa = wishlistdb.objects.filter(uname=request.session['name'])
        x = 0
        for i in dataa:
            x += 1
        if request.method == "POST":
            pp = request.POST.get('pro')
        data = itemdb.objects.filter(Q(cname__icontains=pp) | Q(iname__icontains=pp))
        return render(request, "shop.html", {'data': data, 'x': x})
    else:
        if request.method == "POST":
            pp = request.POST.get('pro')
        data = itemdb.objects.filter(Q(cname__icontains=pp) | Q(iname__icontains=pp))
    return render(request, "shop.html", {'data': data})



