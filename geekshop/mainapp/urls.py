from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('<int:page>/', mainapp.catalog, name='index'),
    path('category/<int:pk>/page/<int:page>/', mainapp.catalog, name='catalog'),
    path('item/<int:pk>/', mainapp.product, name='product')
]
