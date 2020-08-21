from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Breed, Cat

# Create your views here.

class CatList(LoginRequiredMixin, View) :
    def get(self, request):
        bc = Breed.objects.all().count();
        cl = Cat.objects.all();

        ctx = { 'breed_count': bc, 'cat_list': cl };
        return render(request, 'cats/cat_list.html', ctx)

class BreedView(LoginRequiredMixin,View) :
    def get(self, request):
        bl = Breed.objects.all();
        ctx = { 'breed_list': bl };
        return render(request, 'cats/cat_list.html', ctx)

# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded

class CatCreate(LoginRequiredMixin,CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedCreate(LoginRequiredMixin, CreateView):
  model = Breed
  fields = '__all__'
  success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
  model = Breed
  fields = '__all__'
  success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
  model = Breed
  fields = '__all__'
  success_url = reverse_lazy('cats:all')

# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#createview

