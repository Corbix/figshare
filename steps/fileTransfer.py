from behave import *
from utils import *

@when(u'upload file from "{path}"')
def step_impl(context,path):
    context.driver.find_element_by_xpath("//input[@type='file']").send_keys(path) # as fi preferat sa folosesc os.path.realpath('../../test.txt') dar nu reusesc sa-l fac sa mearga

    context.driver.find_element_by_xpath('//span[text()="Save changes"]').click()

    import time
    time.sleep(1) # Varianta romaneasca (merge si asa)

    """try: # Provoaca o exceptie destul de urata

        ''' # required libraries
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        '''

        #element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//span[text()="Save changes"]')))

        WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//span[text()="Save changes"]')))

    finally:
        context.driver.quit()"""


    context.driver.find_element_by_xpath('//a[text()="Cancel"]').click()

@then(u'file is visible')
def step_impl(context):
    assert context.driver.find_element_by_xpath('//a[text()="test.txt"]').is_displayed() is True

@when(u'delete file')
def step_impl(context):
    context.driver.find_element_by_xpath('//a[text()="test.txt"]').click()

    context.driver.find_element_by_xpath('//a[text()="Delete item"]').click()

    context.driver.find_element_by_xpath('//a[text()="Yes, delete"]').click()



@then(u'file is not visible')
def step_impl(context):
    #assert context.driver.find_element_by_xpath('//a[text()="test.txt"]').is_displayed() is None
    from selenium.common.exceptions import NoSuchElementException
    try:
        context.driver.find_element_by_xpath('//a[text()="test.txt"]')
        assert False
    except NoSuchElementException:
        assert True
