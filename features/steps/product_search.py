from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given("User is on homepage")
def step_impl(context):
    context.driver.get(context.base)
    context.driver.set_window_size(1920, 1080)

@when('User enters Iphone in the search bar')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("Iphone")
    context.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)

@then('User should see Iphone product in the results')
def step_impl(context):
    # find iphone image
    element = context.driver.find_element(By.XPATH, r'//*[@id="product-list"]/div/form/div/div[1]/a/img')

@given('User searched for an Iphone')
def step_impl(context):
    context.driver.get(context.base)
    context.driver.set_window_size(1920, 1080)
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("Iphone")
    context.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)

@when("User opens first search result")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#product-list > div:nth-child(1) > form > div > div.image').click()
    pass

@then('User should see product detail of Iphone')
def step_impl(context):
    assert 'en-gb/product' in context.driver.current_url
    pass
