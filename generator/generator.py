from data.data import AuthForm
from locators.checkboxes_page_locators import CheckboxesPageLocators
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

def generated_random_checkbox():
    LIST_CHECKBOXES = CheckboxesPageLocators.LIST_CHECKBOX
    return random.choice(LIST_CHECKBOXES)

def generated_random_dropdown_value():
    #value = ['Option 1', 'Option 2']
    return str(random.randint(1, 2))