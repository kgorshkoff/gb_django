from django.shortcuts import render
import datetime
import json
import os


def main_view(request):
    title = 'Главная'
    content = {'title': title}
    return render(request, 'index.html', content)


def catalog(request):
    title = 'Каталог'

    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'static', 'data.json'))
    with open(path) as json_data:
        products = json.load(json_data)


    content = {'title': title, 'products': products}
    return render(request, 'catalog.html', content)


def contacts(request):
    title = 'Контакты'
    content = {'title': title}
    return render(request, 'contacts.html', content)
