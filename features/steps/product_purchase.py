from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import time

@given("User is on a product detail of a product that is in stock")
def step_impl(context):
    context.driver.get(context.base)
    context.driver.find_element(By.XPATH, r'//*[@id="content"]/div[2]/div[2]/form/div/div[1]/a/img').click()

    # verify is in stock
    availability_text = context.driver.find_element(By.XPATH, r'//*[@id="content"]/div[1]/div[2]/ul[1]/li[3]')
    assert availability_text.text == 'Availability: In Stock'

@when("User adds product to his shopping cart")
def step_impl(context):
    context.driver.find_element(By.XPATH, r'//*[@id="button-cart"]').click()

    # hide notification
    context.driver.find_element(By.XPATH, r'//*[@id="alert"]/div/button').click()

@then("Product is in user's shopping cart")
def step_impl(context):
    # click on shopping cart contents
    context.driver.find_element(By.XPATH, '//*[@id="header-cart"]/div/button').click()

    # check there is one item in shopping cart
    cart_item = context.driver.find_element(By.XPATH, '//*[@id="header-cart"]/div/ul/li/table/tbody/tr/td[2]/a')
    
@given("User's shopping cart is not empty")
def step_impl(context):
    #TODO implement this
    pass

@given("User is on checkout page")
def step_impl(context):
    #TODO implement this
    pass

@when("User fills in all necessary data")
def step_impl(context):
    #TODO implement this
    pass

@then("User can place the order")
def step_impl(context):
    #TODO implement this
    pass
