# -- FILE:features/steps/main.py

from selenium import webdriver
from behave import *

@given('firefox web browser is installed')
def step_impl(context):
    pass

@when('pluto.tv is reachable')
def step_impl(context):
    context.browser.get('https://pluto.tv/')

@then('test pluto.tv main page')
def step_impl(context):
    assert context.browser.title == "Pluto TV - It's Free TV"
    #assert context.browser.title == "Pluto TV"
