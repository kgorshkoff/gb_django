from django.test import TestCase
import hashlib
import random


email = 'test@test.com'
# Create your tests here.
salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
activation_key = hashlib.sha1((email + salt).encode('utf8')).hexdigest()

print(activation_key)
