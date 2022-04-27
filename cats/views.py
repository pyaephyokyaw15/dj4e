from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat, Breed

# Create your views here.


class CatView(LoginRequiredMixin, View):
    def get(self, request):
        breed_count = Breed.objects.all().count()
        cats = Cat.objects.all()

        ctx = {'breed_count': breed_count, 'cat_list': cats}
        return render(request, 'cats/cat_list.html', ctx)


class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        breed_list = Breed.objects.all()
        ctx = {'breed_list': breed_list}
        return render(request, 'cats/breed_list.html', ctx)


