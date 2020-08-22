from django.shortcuts import render
from django.urls import reverse_lazy

from . import owner
from .models import Ad

# Create your views here.

class AdListView(owner.ListView):
    model = Ad

class AdDetailView(owner.DetailView):
    model = Ad

class AdCreateView(owner.CreateView):
    model = Ad
    fields = ['title', 'price', 'text']

class AdUpdateView(owner.UpdateView):
    model = Ad
    fields = ['title', 'price', 'text']


class AdDeleteView(owner.DeleteView):
    model = Ad

