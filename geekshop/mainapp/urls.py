from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('<int:page>/', mainapp.CatalogView.as_view(), name='index'),
    path('category/<int:pk>/page/<int:page>/', mainapp.CatalogView.as_view(), name='catalog'),
    path('item/<int:pk>/', mainapp.ProductView.as_view(), name='product')
]
