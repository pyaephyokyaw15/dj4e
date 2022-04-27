from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'cats'
urlpatterns = [
    path('', views.CatView.as_view(), name='all'),
    path('lookup/', views.BreedView.as_view(), name='breed_list'),

]