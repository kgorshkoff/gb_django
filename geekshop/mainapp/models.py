from django.db import models


class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=32, unique=True, verbose_name='Название')
    image = models.ImageField(upload_to='products', verbose_name='Изображение', null=True)
    position = models.PositiveIntegerField(verbose_name='Порядок')
    is_active = models.BooleanField(verbose_name='Активность')


class Product(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=32, unique=True, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='products', verbose_name='Изображение', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(verbose_name='Активность')
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)


# one to one = OneToOne
# one to many = ForeignKey
# many to many = ManyToMany

