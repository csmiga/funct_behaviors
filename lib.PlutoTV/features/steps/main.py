# -- FILE:features/steps/main.py

#import time
#import os
from selenium import webdriver
from behave import *

@given('firefox web browser is installed')
def step_impl(context):
    pass

@when('pluto.tv is reachable')
def step_impl(context):
    #options = webdriver.FirefoxOptions()
    #options.add_argument('--headless')
    #options.binary_location = '/usr/bin/firefox'

    #context.browser = webdriver.Firefox(firefox_options=options)
    #context.browser.implicitly_wait(10)

    context.browser.get('https://pluto.tv/')

@then('test pluto.tv main page')
def step_impl(context):
    assert context.browser.title == "Pluto TV - It's Free TV"
