from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Product
from .models import Category


def main_view(request, page=1):
    queryset = Category.objects.all().exclude(is_active=False)
    queryset = queryset.order_by('position')

    paginator = Paginator(queryset, 4)
    try:
        categories_paginator = paginator.page(page)
    except PageNotAnInteger:
        categories_paginator = paginator.page(1)
    except EmptyPage:
        categories_paginator = paginator.page(paginator.num_pages)

    content = {'categories': categories_paginator, 'basket': get_basket(request.user)}
    return render(request, 'mainapp/index.html', content)


def catalog(request, pk=None, page=1):
    title = 'Каталог'
    products = Product.objects.all().exclude(is_active=False)

    if pk:
        if pk == 0:
            products = Product.objects.all().order_by('price', is_active=True)
        else:
            products = Product.objects.filter(category__pk=pk, is_active=True).order_by('price')

    paginator = Paginator(products, 6)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    content = {'title': title, 'products': products_paginator, 'basket': get_basket(request.user)}
    return render(request, 'mainapp/catalog.html', content)


def product(request, pk):
    product = Product.objects.filter(pk=pk)
    content = {'product': product}
    return render(request, 'mainapp/product.html', content)


def contacts(request):
    title = 'Контакты'
    content = {'title': title, 'basket': get_basket(request.user)}
    return render(request, 'mainapp/contacts.html', content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []
