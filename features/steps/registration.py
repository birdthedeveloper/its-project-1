from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

credentials = {
    "email":"noooo@gmail.com",
    "pwd":"heslo"
}

# idempotent user creation
@given("User has an account")
def step_impl(context):
    
    context.driver.get(context.base)
    context.driver.set_window_size(1920, 1080)
    context.driver.find_element(By.XPATH, r'//*[@id="top"]/div/div[2]/ul/li[2]/div/a/i[2]').click()
    time.sleep(1)
    context.driver.find_element(By.LINK_TEXT, "Register").click()
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("martin")
    context.driver.find_element(By.ID, "input-lastname").click()
    context.driver.find_element(By.ID, "input-lastname").send_keys("xptace20")
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys(credentials["email"])
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys(credentials["pwd"])
    context.driver.find_element(By.NAME, "agree").click()
    context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    # if nothing happened, user already exists, go to homepage
    time.sleep(1)
    if 'register' in context.driver.current_url:
        context.driver.get(context.base)
    else:
        # sign user out and go to homepage
        context.driver.find_element(By.CSS_SELECTOR, ".img-fluid").click()
        context.driver.find_element(By.XPATH, r'//*[@id="top"]/div/div[2]/ul/li[2]/div/a/i[2]').click()
        context.driver.find_element(By.LINK_TEXT, "Logout").click()
        context.driver.find_element(By.LINK_TEXT, "Continue").click()


@when("User enters right credentials into log in page")
def step_impl(context):
    context.driver.get(context.base)
    context.driver.set_window_size(1920, 1080)
    context.driver.find_element(By.XPATH, r'//*[@id="top"]/div/div[2]/ul/li[2]/div/a/i[2]').click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys(credentials["email"])
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys(credentials["pwd"])
    context.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()
  

@then("User should be signed in")
def step_impl(context):
    time.sleep(1)
    assert 'account&customer_token=' in context.driver.current_url
