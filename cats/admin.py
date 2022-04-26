from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Cat, Breed

admin.site.register(Cat)
admin.site.register(Breed)