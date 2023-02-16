from django.contrib import admin
from .models import category


class CategoryaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')


admin.site.register(category, CategoryaAdmin)