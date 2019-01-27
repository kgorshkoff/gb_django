from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.catalog, name='index'),
    path('category/<int:pk>', mainapp.catalog, name='catalog'),
    path('<int:pk>', mainapp.product, name='product')
]
