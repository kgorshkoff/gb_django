from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Product
from .models import Category


def main_view(request):
    queryset = Category.objects.all().exclude(is_active=False)
    queryset = queryset.order_by('position')
    content = {'categories': queryset, 'basket': get_basket(request.user)}
    return render(request, 'mainapp/index.html', content)


def catalog(request, pk=None):
    title = 'Каталог'
    products = Product.objects.all().exclude(is_active=False)

    if pk:
        if pk == 0:
            products = Product.objects.all().order_by('price').exclude(is_active=False)
        else:
            products = Product.objects.filter(category__pk=pk).order_by('price').exclude(is_active=False)

    content = {'title': title, 'products': products, 'basket': get_basket(request.user)}
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
