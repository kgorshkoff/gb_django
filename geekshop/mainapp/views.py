from django.shortcuts import render
import datetime
import json
import os


def main_view(request):
    title = 'Главная'
    date = datetime.date.today().year
    content = {'date': date, 'title': title}
    return render(request, 'index.html', content)


def catalog(request):
    title = 'Каталог'
    date = datetime.date.today().year

    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'static', 'data.json'))
    with open(path) as json_data:
        products = json.load(json_data)
        json_data.close()

    content = {'title': title, 'products': products, 'date': date}
    return render(request, 'catalog.html', content)


def contacts(request):
    title = 'Контакты'
    date = datetime.date.today().year
    content = {'title': title, 'date': date}
    return render(request, 'contacts.html', content)
