from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='client_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', blank=True, null=True)
    email = models.EmailField(verbose_name='почта', unique=True)
    active_key = models.CharField(max_length=128, verbose_name='код подтверждения', blank=True)
    active_key_expires = models.DateTimeField(default=timezone.now() + timezone.timedelta(48))

    def is_activation_key_expired(self):
        if timezone.now() <= self.active_key_expires:
            return False
        else:
            return True


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICE = (
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина')
    )

    RUSSIAN = 'ru'
    ENGLISH = 'en'

    LANGUAGE_CHOICE = (
        (RUSSIAN, 'Русский'),
        (ENGLISH, 'English')
    )

    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='тэги', max_length=128, blank=True)
    about_me = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICE, blank=True)
    language = models.CharField(verbose_name='язык', choices=LANGUAGE_CHOICE, max_length=20, blank=False, default='ru')

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
