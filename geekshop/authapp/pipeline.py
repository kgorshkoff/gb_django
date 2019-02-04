import requests
import random, string
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from social_core.exceptions import AuthForbidden


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        if 'gender' in response.keys():
            if response['gender'] == 'male':
                user.shopuserprofile.gender = 'M'
            else:
                user.shopuserprofile.gender = 'W'

        if 'tagline' in response.keys():
            user.shopuserprofile.tagline = response['tagline']

        if 'aboutMe' in response.keys():
            user.shopuserprofile.about_me = response['aboutMe']

        if 'ageRange' in response.keys():
            minAge = response['ageRange']['min']
            if int(minAge) < 18:
                user.delete()
                raise AuthForbidden('social_core.backends.google.GoogleOAuth2')

        if 'picture' in response.keys():
            seed = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            url = response['picture']

            r = requests.get(url)
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(r.content)
            img_temp.flush()
            user.avatar.save(seed + '.' + response['picture'].split('.')[-1], File(img_temp), save=True)

        if 'language' in response.keys():
            if response['locale'] == 'ru':
                user.shopuserprofile.language = 'ru'
            else:
                user.shopuserprofile.language = 'en'

        user.save()

    return
