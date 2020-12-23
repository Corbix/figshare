from behave import *
from utils import *

@given(u'{browser} is opened')
def step_impl(context,browser):
    context.driver=browserLaunch(browser)
    context.driver.implicitly_wait(10)

@when(u'load site')
def step_impl(context):
    context.driver.get("https://figshare.com/")


@when(u'we log in with username "{usr}" and password "{pwd}"')
def step_impl(context,usr,pwd):
    context.driver.find_element_by_xpath('//a[contains(@href,"https://figshare.com/account/login")]').click() # click login button

    context.driver.find_element_by_xpath('//input[contains(@autocomplete,"email")]').send_keys(usr) # enter username

    context.driver.find_element_by_xpath('//input[contains(@autocomplete,"password")]').send_keys(pwd) # enter password

    context.driver.find_element_by_xpath('//button[contains(@type,"submit")]').click() #click submit


@then(u'invalid credentials shows up')
def step_impl(context):
    assert context.driver.find_element_by_xpath('//span[text()="Invalid credentials"]').is_displayed() is True

@then(u'valid credentials shows up')
def step_impl(context):
    assert context.driver.find_element_by_xpath('//img[contains(@title,"bqk79730 bqk79730")]').is_displayed() is True


@then(u'logout')
def step_impl(context):
    context.driver.find_element_by_xpath('//img[contains(@title,"bqk79730 bqk79730")]').click()
    context.driver.find_element_by_xpath('//a[contains(@href,"https://figshare.com/account/logout")]').click()

@then(u'close')
def step_impl(context):
    context.driver.close()
