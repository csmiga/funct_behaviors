# -- FILE:features/environment.py

"""
This module contains environment controls:
http://behave.readthedocs.io/en/latest/api.html#environment-file-functions

The functions handle Selenium WebDriver setup and cleanup.

(Alternatively, fixtures could be used:
http://behave.readthedocs.io/en/latest/fixtures.html)
"""

from selenium import webdriver

# Hooks
# Firefox is the hard-coded browser of choice. Feel free to change it here.
# The correct browser and WebDriver executable must be installed on the test
# machine. A flexible framework would read the browser choice from inputs or
# config data.

def before_tag(context, tag):
    if tag.startswith("browser."):
        browser_type = tag.replace("browser.", "", 1)
        if browser_type == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            options.binary_location = '/usr/bin/firefox'
            context.browser = webdriver.Firefox(firefox_options=options)
            context.browser.implicitly_wait(10)
        elif browser_type == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument("--test-type")
            options.binary_location = '/usr/bin/chromium-browser'
            context.browser = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=options)
            context.browser.implicitly_wait(10)
        else:
            context.browser = webdriver.PlainVanilla()
            context.browser.implicitly_wait(10)

def after_tag(context, tag):
    if tag.startswith("browser."):
        browser_type = tag.replace("browser.", "", 1)
        if browser_type == "firefox":
            context.browser.quit()
        elif browser_type == "chrome":
            context.browser.quit()
        else:
            context.browser.quit()