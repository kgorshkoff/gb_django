from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserProfileEditForm
from django.contrib import auth
from django.urls import reverse
from django.conf import settings

from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser


def send_verify_mail(user):
    title = 'Подтверждение регистрации'
    verify_link = reverse('authapp:verify', args=[user.email, user.active_key])
    message = 'Для подтверждения на портале {domain_name} перейдите по ссылке {domain_name}{link}'\
        .format(domain_name = settings.DOMAIN_NAME, link = verify_link)
    from_address = 'djangolesson2019@yandex.ru'
    return send_mail(title, message, from_address, [user.email], fail_silently=False)


def login(request):
    title = 'Вход'

    login_form = ShopUserLoginForm(data=request.POST or None)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print('mail sent')
            else:
                print('mail NOT sent')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content)


@transaction.atomic
def edit(request):
    title = 'Редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, request.FILES, instance=request.user.shopuserprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    content = {'title': title, 'edit_form': edit_form, 'profile_form': profile_form}

    return render(request, 'authapp/edit.html', content)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.active_key == activation_key and not user.is_activation_key_expired():
            print(f'user {user} is activated')
            user.is_active = True
            user.save()
            auth.login(request, user)

            return render(request, 'authapp/verification.html')
        else:
            print(f'error activating user: {user}')
            return render(request, 'authapp/verification.html')

    except Exception as e:
        print(f'error activating user : {e.args}')

    return HttpResponseRedirect(reverse('main'))
