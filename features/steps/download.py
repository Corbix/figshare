from behave import *
from utils import *
import time
import random

@given(u'we are on the landing page')
def step_impl(context):
    context.driver.get("https://figshare.com/")
    context.list=os.listdir(".") # iau lista fisierelor din folderul in care voi descarca (pentru a verifica adaugarea noilor fisiere)


@when(u'we select a random article')
def step_impl(context):
    random.choice(context.driver.find_elements_by_xpath('//div[contains(@role,"article")]')).click() # fac o lista cu toate articolele vizibile pe pagina principala si folosesc un algoritm din libraria random pentru a alege una singura

@when(u'we download it')
def step_impl(context):
    #driver.find_element_by_xpath('//span[text()="Download"]').click()

    context.driver.execute_script("arguments[0].click();", context.driver.find_element_by_xpath('//span[text()="Download"]'))
    time.sleep(10) # astept terminarea descarcarii, altfel se descarca partial sau deloc

@then(u'file is accessible in the filesystem')
def step_impl(context):
    assert not context.list==os.listdir(".") # Verific daca au aparut fisierul nou (argumentul ar trebui sa fie calea catre folderul de descarcare implicit pentru webdriver)
