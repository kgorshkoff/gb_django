from django.contrib import admin
from .models import Product
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    ordering = ('position', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
