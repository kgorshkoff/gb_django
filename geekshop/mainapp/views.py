import json
import os

from django.shortcuts import render
from .models import Product
from .models import Category


def main_view(request):
    queryset = Category.objects.all()
    queryset = queryset.order_by('position')
    content = {'categories': queryset}
    return render(request, 'index.html', content)


def catalog(request):
    title = 'Каталог'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    return render(request, 'catalog.html', content)


def catalog_id(request, category_id):
    title = 'Каталог'
    products = Product.objects.filter(category=category_id)
    content = {'title': title, 'products': products}
    return render(request, 'catalog.html', content)


def contacts(request):
    title = 'Контакты'
    content = {'title': title}
    return render(request, 'contacts.html', content)
