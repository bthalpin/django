import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker
import random

fake_generator = Faker()

def populate(N=5):
    for num in range(N):
        first = fake_generator.first_name()        
        last = fake_generator.last_name()        
        email = fake_generator.email()

        User.objects.get_or_create(first_name = first,last_name=last,email=email)

if __name__=='__main__':
    populate(20)