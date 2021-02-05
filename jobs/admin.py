from django.contrib import admin
from .models import Job


# admin.site.register(Job)


@admin.register(Job)
class PetAdmin(admin.ModelAdmin):
    list_display = ['title', 'sort_order', 'summary']
