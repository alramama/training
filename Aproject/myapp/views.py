from django.shortcuts import render

# Create your views here.
# app/views.py

from django.shortcuts import render
from .models import BookLibrary

def index(request):
    context = BookLibrary.objects.all()
    return render(request, 'app/list_books.html', {'context': context})

# app/views.py

from django.shortcuts import render, redirect
from .forms import BookLibForm

def add_book(request):
    template = 'app/add_books.html'
    form = BookLibForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, template, context)

from django.shortcuts import render, redirect, get_object_or_404

def edit_book(request, pk):
    template = 'app/edit_books.html'
    book = get_object_or_404(BookLibrary, pk=pk)
    form = BookLibForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, template, context)

# app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import BookLibrary


def delete_book(request, pk):
    template = 'app/delete_books.html'
    obj = get_object_or_404(BookLibrary, pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('/')
    context = {"book": obj}
    return render(request, template, context)