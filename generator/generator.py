from data.data import AuthForm
from faker import Faker
import random
import os

faker_en = Faker('En')
faker_ru = Faker('Ru')

def generated_count_clicks_to_add_button():
    generated_count = random.randint(10, 20)
    return generated_count

def generated_auth_form():
    yield AuthForm(login=faker_en.name_male(), password=faker_en.name_male())

def generated_random_broken_image():
    return random.randint(1, 3)