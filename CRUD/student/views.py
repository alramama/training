from django.shortcuts import render
import mimetypes

from django.shortcuts import render ,redirect
from student.forms import *
from student.models import *
from django.http import HttpResponse
from django.contrib import messages
import os
# Import HttpResponse module
from django.http.response import HttpResponse

def show_stud(request):
    bid = Stud.objects.order_by('-id');
    return render(request, 'index.html', {'bid':bid})

"""
def create_stud(request):
    form = StudForm()
    if request.method == "POST":
        form = StudForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Created successful!")
                return redirect('/show_stud')
            except:
                message = "Something we are wrong!"
                form = StudForm()
            return render(request, 'create.html',{'message':message,'form':form})
    else:
        form = StudForm()
    return render(request, 'create.html',{'form':form})


def edit_stud(requst, id):
    stud = Stud.objects.get(id=id)
    return render(requst, 'edit.html',{'stud':stud})

def update_stud(request, id):
    stud = Stud.objects.get(id=id)
    if request.method == "POST" :
        form = StudForm(request.POST, request.FILES, instance = stud)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful!')
            return redirect("/show_stud")
        message = 'Something we are wrong!'
        return render(request, 'edit.html',{'message':message,'stud':form})
    else:
        form = Stud.objects.get(id=id)
        stud = StudForm(instance = form)
        content = {'stud':stud,'id':id}
        return render(request, 'edit.html',content)

def delete_stud(request, id):
    stud = Stud.objects.get(id=id)
    stud.delete()
    messages.success(request, 'Deleted successful!')
    return redirect("/show_stud")

def index1(request):
    if request.method=='POST':
        upload1 = request.FILES['Stud']
        object = Stud.objects.create(upload=upload1)
        object.save()
    context = Stud.objects.all()
    return render(request,'index1.html',{'context':context})

"""
