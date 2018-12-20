import json
import os

from django.shortcuts import render

from basketapp.models import Basket
from .models import Product
from .models import Category


def main_view(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    queryset = Category.objects.all()
    queryset = queryset.order_by('position')
    content = {'categories': queryset, 'basket': basket}
    return render(request, 'index.html', content)


def catalog(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    title = 'Каталог'
    products = Product.objects.all()
    content = {'title': title, 'products': products, 'basket': basket}
    return render(request, 'catalog.html', content)


def catalog_id(request, category_id):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    title = 'Каталог'
    products = Product.objects.filter(category=category_id)
    content = {'title': title, 'products': products, 'basket': basket}
    return render(request, 'catalog.html', content)


def contacts(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    title = 'Контакты'
    content = {'title': title, 'basket': basket}
    return render(request, 'contacts.html', content)
