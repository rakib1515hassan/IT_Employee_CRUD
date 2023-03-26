import os

from django.shortcuts import render, redirect
from .models import profile
from django.db.models import Q


def login(r):
    if r.method == 'POST':
        name = r.POST['name']
        email = r.POST['email']
        img = r.FILES['fileupload']
        user = profile.objects.create(name=name, email=email, proPic=img)
        user.save()

    return render(r, 'login.html', locals())


def Prof(r):
    pro = profile.objects.all()
    return render(r, 'newProf.html', locals())

def delete(r,id):
    pro= profile.objects.get(id=id)
    if len(pro.proPic)>0:
        os.remove(pro.proPic.path)
        pro.delete()
    return redirect('Prof')


def update(r, id):
    pro = profile.objects.get(id=id)
    if r.method == 'POST':
        name = r.POST.get('name')
        email = r.POST.get('email')
        proPic = r.FILES.get('fileupload')



        if len(r.FILES)!= 0:
            if len(pro.proPic) > 0:
                os.remove(pro.proPic.path)
            pro.proPic = proPic

        pro.name = name
        pro.email = email

        pro.save()
        return redirect('Prof')

    return render(r, 'Update.html', {'pro': pro})

def search(request):
    if request.method == "POST":
        query=request.POST.get("search")
        if query:
            query_set =(Q(name__icontains = query))|(Q(email__icontains = query))
            pro = profile.objects.filter(query_set).distinct()
        else:
            pro = []
    return render(request, 'newProf.html', {"pro":pro})

