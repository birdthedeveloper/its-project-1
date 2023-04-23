from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time


def go_to_detail_in_stock(context):
    context.driver.get(context.base)
    context.driver.find_element(By.XPATH, r'//*[@id="content"]/div[2]/div[2]/form/div/div[1]/a/img').click()

    # verify is in stock
    availability_text = context.driver.find_element(By.XPATH, r'//*[@id="content"]/div[1]/div[2]/ul[1]/li[3]')
    assert availability_text.text == 'Availability: In Stock'

def add_to_shopping_cart(context):
    context.driver.find_element(By.XPATH, r'//*[@id="button-cart"]').click()

    # hide notification
    context.driver.find_element(By.XPATH, r'//*[@id="alert"]/div/button').click()

@given("User is on a product detail of a product that is in stock")
def step_impl(context):
    go_to_detail_in_stock(context)

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
    go_to_detail_in_stock(context)
    add_to_shopping_cart(context)

@given("User is on checkout page")
def step_impl(context):
    context.driver.get(context.base + '/en-gb?route=checkout/checkout')

@when("User fills in all necessary data")
def step_impl(context):
    context.driver.set_window_size(1920, 1080)

    # guest
    context.driver.find_element(By.XPATH, r'//*[@id="input-guest"]').click()

    # inputs
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("Martin")
    context.driver.find_element(By.ID, "input-lastname").click()
    context.driver.find_element(By.ID, "input-lastname").send_keys("Ptacek")
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys("neexistuje@gmail.com")
    context.driver.find_element(By.ID, "input-shipping-address-1").click()
    context.driver.find_element(By.ID, "input-shipping-address-1").send_keys("Zahumni")
    context.driver.find_element(By.ID, "input-shipping-address-2").click()
    context.driver.find_element(By.ID, "input-shipping-city").click()
    context.driver.find_element(By.ID, "input-shipping-city").send_keys("Breclav")
    context.driver.find_element(By.ID, "input-shipping-postcode").click()
    context.driver.find_element(By.ID, "input-shipping-postcode").send_keys("666666")
    dropdown = context.driver.find_element(By.ID, "input-shipping-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Argyll and Bute']").click()
    element = context.driver.find_element(By.ID, "input-shipping-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = context.driver.find_element(By.ID, "input-shipping-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.ID, "input-shipping-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).release().perform()
    webdriver.ActionChains(context.driver).send_keys(Keys.ESCAPE).perform()

    # scroll down
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1) # mandatory

    context.driver.find_element(By.XPATH, r'//*[@id="input-newsletter"]').click()
    context.driver.find_element(By.XPATH, r'//*[@id="input-register-agree"]').click()
    context.driver.find_element(By.ID, "button-register").click()

    # scroll up
    context.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
    
    time.sleep(2) # wait for scroll to happen
     
    # close notification
    context.driver.find_element(By.XPATH, r'//*[@id="alert"]/div/button').click()

    context.driver.find_element(By.XPATH, r'//*[@id="button-shipping-methods"]').click()

    # shipping dialog
    context.driver.find_element(By.CSS_SELECTOR, r'#input-shipping-method-flat-flat').click()
    context.driver.find_element(By.CSS_SELECTOR, r'#button-shipping-method').click()


    # payment method
    context.driver.find_element(By.XPATH, r'//*[@id="button-payment-methods"]').click()

    context.driver.find_element(By.CSS_SELECTOR, r'#input-payment-method-cod-cod').click()
    context.driver.find_element(By.CSS_SELECTOR, r'#button-payment-method').click()

    # finish
    context.driver.find_element(By.ID, "input-comment").click()
    context.driver.find_element(By.ID, "input-comment").send_keys("This is an order comment")
    context.driver.find_element(By.ID, "button-confirm").click()

@then("User can place the order")
def step_impl(context):

    # mandatory wait
    time.sleep(1)
    assert 'checkout/success' in context.driver.current_url
