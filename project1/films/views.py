from django.shortcuts import render

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BID

class BIDBaseView(View):
    model = BID
    fields = '__all__'
    success_url = reverse_lazy('films:all')

class BIDListView(BIDBaseView, ListView):
    """View to list all films.
    Use the 'film_list' variable in the template
    to access all BID objects"""

class BIDDetailView(BIDBaseView, DetailView):
    """View to list the details from one film.
    Use the 'film' variable in the template to access
    the specific film here and in the Views below"""

class BIDCreateView(BIDBaseView, CreateView):
    """View to create a new film"""

class BIDUpdateView(BIDBaseView, UpdateView):
    """View to update a film"""

class BIDDeleteView(BIDBaseView, DeleteView):
    """View to delete a film"""
from django.http import FileResponse

def index1(request):
    if request.method=='POST':
        upload1 = request.FILES['BID']
        object = BID.objects.create(upload=upload1)
        object.save()
    context = BID.objects.all()
    return render(request,'bid_list.html',{'context':context})
