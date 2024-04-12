from django.shortcuts import render,redirect
from manu.models import categorydb,itemdb
from frontend.models import contactdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def categoryreg(request):
    return render(request,"register.html",)

def save(request):
    if request.method == "POST":
        aa = request.POST.get('n')
        gg = request.POST.get('d')
        hh = request.FILES['img']
        obj = categorydb(name=aa,details=gg,image=hh)
        obj.save()
        messages.success(request, "Category Sucessfully Saved.!")
        return redirect(categoryreg)

def disp(request):
    data = categorydb.objects.all()
    return render(request,"table.html",{'data':data})

def edit(request,sid):
    std = categorydb.objects.get(id=sid)
    return render(request,"edit.html",{'std':std})

def eupload(request,sid):
    if request.method == "POST":
        aa = request.POST.get('n')
        gg = request.POST.get('d')
        try:
            i = request.FILES["img"]
            fs = FileSystemStorage()
            file = fs.save(i.name,i)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=sid).image
        categorydb.objects.filter(id=sid).update(name=aa,details=gg,image=file)
        messages.success(request, "Updated Sucessfully.!")
        return redirect(disp)

# item functions

def creg(request):
    data = categorydb.objects.all()
    return render(request,"ireg.html",{'data':data})

def cupload(request):
    if request.method == "POST":
        aa = request.POST.get('cn')
        tt = request.POST.get('in')
        ff = request.POST.get('p')
        dd = request.POST.get('d')
        ii = request.FILES['img']
        mm = request.FILES['img1']
    obj = itemdb(cname=aa,iname=tt,price=ff,details=dd,image=ii,image1=mm)
    obj.save()
    messages.success(request, "Item Sucessfully Saved.!")
    return redirect(creg)

def ctable(request):
    item = itemdb.objects.all()
    return render(request,"ctb.html",{'item':item})

def cedit(request,cid):
    data = itemdb.objects.get(id=cid)
    cat = categorydb.objects.all()
    return render(request,"itemedit.html",{'data':data,'cat':cat})

def cepload(request,cid):
    if request.method == "POST":
        aa = request.POST.get('cn')
        tt = request.POST.get('in')
        ff = request.POST.get('p')
        dd = request.POST.get('d')
        try:
            i = request.FILES["img"]
            fs = FileSystemStorage()
            file = fs.save(i.name,i)
        except MultiValueDictKeyError:
            file = itemdb.objects.get(id=cid).image
        try:
            j = request.FILES["img1"]
            fs = FileSystemStorage()
            file1 = fs.save(j.name,j)
        except MultiValueDictKeyError:
            file1 = itemdb.objects.get(id=cid).image1
        itemdb.objects.filter(id=cid).update(cname=aa,iname=tt,price=ff,details=dd,image=file,image1=file1)
        messages.success(request, "Item Sucessfully.!")
        return redirect(ctable)

def cdel(request,cid):
    x = (itemdb.objects.filter(id=cid))
    x.delete()
    messages.success(request, "Deleted Sucessfully.!")
    return redirect(ctable)

def sdel(request,sid):
    x = (categorydb.objects.filter(id=sid))
    x.delete()
    messages.success(request, "Deleted Sucessfully.!")
    return redirect(disp)

def adlog(request):
    return render(request,"alogin.html")

def adlogin(request):
    if request.method == "POST":
        uu = request.POST.get('un')
        pp = request.POST.get('ps')
        if User.objects.filter(username__contains=uu).exists():
            x = authenticate(username=uu,password=pp)
            if x is not None:
                login(request,x)
                request.session['username'] = uu
                request.session['password'] = pp
                messages.success(request, "Login Sucessfully.!")
                return redirect(index)
            else:
                messages.error(request, "Invalid password.!")
                return redirect(adlog)
        else:
            messages.warning(request, "Invalid Username.!")
            return redirect(adlog)

def adlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Sucessfully.!")
    return redirect(adlog)

def contv(request):
    con = contactdb.objects.all()
    return render(request,"contactv.html",{'con':con})

def cdel(request,cid):
    x=(contactdb.objects.filter(id=cid))
    x.delete()
    messages.success(request, "Deleted Sucessfully.!")
    return redirect(contv)