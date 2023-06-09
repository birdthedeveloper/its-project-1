 #!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException

from behave import fixture, use_fixture

import time

def get_driver():
    '''Get Chrome/Firefox driver from Selenium Hub'''
    try:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
    except WebDriverException:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.FIREFOX)
    driver.implicitly_wait(5)

    # Web stranku ziskate nasledujicim:
    # (jedno nebo druhe, zalezi na nastaveni prostedi)
    # driver.get("http://opencart:8080/")
    # driver.get("http://localhost:8080/")

    return driver

@fixture
def selenium_browser(context):
    context.driver = get_driver()
    context.base = 'http://opencart:8080'
    yield context.driver

    # -- CLEANUP-FIXTURE PART:
    context.driver.quit()

# taken by behave
def before_all(context):
    use_fixture(selenium_browser, context)

def after_scenario(context, scenario):
    interval = 200/1000
    time.sleep(interval)
    context.driver.delete_all_cookies()
    context.driver.get(context.base)
    time.sleep(interval)
