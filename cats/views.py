from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat, Breed

# Create your views here.


class CatList(LoginRequiredMixin, View):
    def get(self, request):
        cat = Cat.objects.all().count()
        breed = Breed.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}
        return render(request, 'cats/cat_list.html', ctx)


class CatCreate(LoginRequiredMixin, View):
    pass


class CatUpdate(LoginRequiredMixin, View):
    pass