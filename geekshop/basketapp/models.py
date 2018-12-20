from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="baskets")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)

# basket = Basket(...)
# print(basket.user)
#
# user = User(...)
# # Корзина
# Basket.objects.filter(user=user)
#
# user.baskets.all()


