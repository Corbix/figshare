from behave import *
from utils import *
#import time

@given(u'we are on the landing page')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given we are on the landing page')
    context.driver.get("https://figshare.com/")
    context.list=os.listdir(".") # iau lista fisielerol din folderul in care voi descarca (pentru a verifica adaugarea noilor fisiere)


@when(u'we select a random article')
def step_impl(context):
    #raise NotImplementedError(u'STEP: When we select a random article')
    random.choice(context.driver.find_elements_by_xpath('//div[contains(@role,"article")]')).click()

@when(u'we download it')
def step_impl(context):
    #raise NotImplementedError(u'STEP: When we download it')

    #driver.find_element_by_xpath('//span[text()="Download"]').click()

    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//span[text()="Download"]'))
    #time.sleep(10)

@then(u'file is accessible in the filesystem')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Then file is accessible in the filesystem')
    assert context.list==os.listdir(".") not True # Verific daca au aparut fisierul nou
