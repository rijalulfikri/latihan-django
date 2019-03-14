import django
import os
from django.utils import timezone
from django.test.utils import setup_test_environment

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'training.settings')
django.setup()

setup_test_environment()

from django.test import Client
# create an instance of the client for our use
client = Client()

# get a response from '/'
response = client.get('/')
response.status_code

from django.urls import reverse
response = client.get(reverse('polls:index'))
response.status_code