#from selenium import webdriver

#def before_all(context):
#    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
#    desired_capabilities['browserName': 'firefox'
#    #desired_capabilities['version'] = '80'
#    #desired_capabilities['platform'] = 'LINUX'
#    #desired_capabilities['name'] = 'Testing Selenium with Behave'
#    #desired_capabilities['client_key'] = 'key'
#    #desired_capabilities['client_secret'] = 'secret'

#    context.browser = webdriver.Remote(
#        desired_capabilities=desired_capabilities,
#        command_executor="http://www.google.com"

#    options = webdriver.FirefoxOptions()
#    options.add_argument('--headless')
#    options.binary_location = '/usr/bin/firefox'

#    )

#def after_all(context):
#    context.browser.quit()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
This module contains environment controls:
http://behave.readthedocs.io/en/latest/api.html#environment-file-functions

The functions handle Selenium WebDriver setup and cleanup.

(Alternatively, fixtures could be used:
http://behave.readthedocs.io/en/latest/fixtures.html)
"""

from selenium import webdriver

# Hooks
# Firefox is the hard-coded browser of choice.
# Feel free to change it here.
# The correct browser and WebDriver executable must be installed on the test
# machine. # A flexible framework would read the browser choice from inputs or
# config data.

def before_scenario(context, scenario):
    if 'web' in context.tags:
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.binary_location = '/usr/bin/firefox'

        context.browser = webdriver.Firefox(firefox_options=options)
        context.browser.implicitly_wait(10)

def after_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser.quit()
