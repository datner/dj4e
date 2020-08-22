from django.contrib import admin

from .models import Category, Site, Iso, Region, State

# Register your models here.

admin.site.register(Category)
admin.site.register(Site)
admin.site.register(Iso)
admin.site.register(Region)
admin.site.register(State)
