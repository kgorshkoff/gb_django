from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.main, name='index'),

    path('users/create/', adminapp.UserCreateView.as_view(), name='user_create'),
    path('users/read/<int:page>', adminapp.UsersListView.as_view(), name='users'),
    path('users/update/<pk>/', adminapp.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<pk>/', adminapp.UserDeleteView.as_view(), name='user_delete'),

    path('categories/create/', adminapp.CategoryCreateView.as_view(), name='category_create'),
    path('categories/read/<int:page>', adminapp.CategoriesListView.as_view(), name='categories'),
    path('categories/update/<pk>/', adminapp.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<pk>/', adminapp.CategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/category/<pk>/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('products/read/category/<pk>/', adminapp.ProductListView.as_view(), name='products'),
    path('products/read/<pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),

]