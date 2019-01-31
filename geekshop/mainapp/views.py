from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from basketapp.models import Basket
from .models import Product
from .models import Category


class MainView(ListView):
    queryset = Category.objects.all().exclude(is_active=False)
    context_object_name = 'categories'
    template_name = 'mainapp/index.html'
    paginate_by = 4
    fields = '__all__'


class CatalogView(ListView):
    queryset = Product.objects.all().exclude(is_active=False)
    context_object_name = 'products'
    template_name = 'mainapp/catalog.html'
    paginate_by = 4


class ProductView(DetailView):
    model = Product
    template_name = 'mainapp/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Product.objects.filter(pk=self.kwargs['pk'])

        return context


def contacts(request):
    title = 'Контакты'
    content = {'title': title}
    return render(request, 'mainapp/contacts.html', content)



