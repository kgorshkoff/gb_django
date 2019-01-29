from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from authapp.models import ShopUser
from mainapp.models import Category, Product
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm

from adminapp.forms import ProductEditForm


@user_passes_test(lambda u: u.is_superuser)
def main(request):
    title = 'админка'
    content = {
        'title': title,
    }

    return render(request, 'adminapp/base.html', content)


class IsSuperuser(object):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def users(request, page=1):
#     title = 'админка/пользователи'
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     paginator = Paginator(users_list, 10)
#     try:
#         users_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         users_paginator = paginator.page(1)
#     except EmptyPage:
#         users_paginator = paginator.page(paginator.num_pages)
#
#     content = {
#         'title': title,
#         'objects': users_paginator
#     }
#
#     return render(request, 'adminapp/users.html', content)


# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     title = 'пользователи/редактирование'
#
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:user_update', args=[edit_user.pk]))
#     else:
#         edit_form = ShopUserAdminEditForm(instance=edit_user)
#
#     content = {'title': title, 'update_form': edit_form}
#
#     return render(request, 'adminapp/user_update.html', content)


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     title = 'пользователи/создание'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('adminapp:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     content = {'title': title, 'update_form': user_form}
#
#     return render(request, 'adminapp/user_update.html', content)


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     title = 'пользователи/удаление'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('adminapp:users'))
#
#     content = {
#         'title': title,
#         'user_to_delete': user
#     }
#
#     return render(request, 'adminapp/user_delete.html', content)


class UserCreateView(CreateView, IsSuperuser):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('adminapp:users')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'пользователи/создание'

        return context


class UsersListView(ListView, IsSuperuser):
    model = ShopUser
    paginate_by = 4
    template_name = 'adminapp/users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'пользователи'

        return context


class UserUpdateView(UpdateView, IsSuperuser):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('adminapp:users')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'пользователи/редактирование'

        return context


class UserDeleteView(DeleteView, IsSuperuser):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('adminapp:users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'пользователи/удаление'

        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def categories(request, page=1):
#     title = 'админка/категории'
#
#     categories_list = Category.objects.all()
#
#     paginator = Paginator(categories_list, 10)
#     try:
#         categories_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         categories_paginator = paginator.page(1)
#     except EmptyPage:
#         categories_paginator = paginator.page(paginator.num_pages)
#
#     content = {
#         'title': title,
#         'objects': categories_paginator
#     }
#
#     return render(request, 'adminapp/categories.html', content)


class CategoryCreateView(CreateView, IsSuperuser):
    model = Category
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/создание'

        return context


class CategoriesListView(ListView, IsSuperuser):
    model = Category
    paginate_by = 4
    template_name = 'adminapp/categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории'

        return context


class CategoryUpdateView(UpdateView, IsSuperuser):
    model = Category
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'

        return context


class CategoryDeleteView(DeleteView, IsSuperuser):
    model = ShopUser
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('adminapp:categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/удаление'

        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     title = 'категории/создание'
#
#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, request.FILES)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('adminapp:categories'))
#     else:
#         category_form = ProductCategoryEditForm()
#
#     content = {'title': title, 'update_form': category_form}
#
#     return render(request, 'adminapp/category_update.html', content)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     title = 'категории/редактирование'
#
#     edit_category = get_object_or_404(Category, pk=pk)
#     if request.method == 'POST':
#         edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:category_update', args=[edit_category.pk]))
#     else:
#         edit_form = ProductCategoryEditForm(instance=edit_category)
#
#     content = {'title': title, 'update_form': edit_form}
#
#     return render(request, 'adminapp/category_update.html', content)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     title = 'категории/удаление'
#
#     category = get_object_or_404(Category, pk=pk)
#
#     if request.method == 'POST':
#         category.is_active = False
#         category.save()
#         return HttpResponseRedirect(reverse('adminapp:categories'))
#
#     content = {'title': title, 'category_to_delete': category}
#
#     return render(request, 'adminapp/category_delete.html', content)


class ProductCreateView(CreateView, IsSuperuser):
    model = Product
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'продукты/создание'

        return context


class ProductUpdateView(UpdateView, IsSuperuser):
    model = Product
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'продукты/редактирование'

        return context


class ProductDeleteView(DeleteView, IsSuperuser):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('adminapp:categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'продукт/удаление'

        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class ProductListView(ListView, IsSuperuser):
    model = Product
    template_name = 'adminapp/products.html'
    # success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'продукты'

        return context


class ProductDetailView(DetailView, IsSuperuser):
    model = Product
    template_name = 'adminapp/product_read.html'



@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(Category, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)


# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     title = 'продукт/подробнее'
#
#     product = get_object_or_404(Product, pk=pk)
#
#     content = {'title': title, 'object': product, }
#
#     return render(request, 'adminapp/product_read.html', content)


# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     title = 'продукт/создание'
#     category = get_object_or_404(Category, pk=pk)
#
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('adminapp:products', args=[pk]))
#     else:
#         # задаем начальное значение категории в форме
#         product_form = ProductEditForm(initial={'category': category})
#
#     content = {'title': title, 'update_form': product_form, 'category': category}
#
#     return render(request, 'adminapp/product_update.html', content)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     title = 'продукт/редактирование'
#
#     edit_product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:product_update', args=[edit_product.pk]))
#     else:
#         edit_form = ProductEditForm(instance=edit_product)
#
#     content = {'title': title, 'update_form': edit_form, 'category': edit_product.category}
#
#     return render(request, 'adminapp/product_update.html', content)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     title = 'продукт/удаление'
#
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('adminapp:products', args=[product.category.pk]))
#
#     content = {
#         'title': title,
#         'product_to_delete': product
#     }
#
#     return render(request, 'adminapp/product_delete.html', content)
