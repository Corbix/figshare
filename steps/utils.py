from selenium import webdriver
import os
import sys

def browserInstalled(browser): # Verific existenta webdriver in locatia executabilului python. Daca returneaza fals, ar trebui sa dau skip la test
    for i in os.listdir("{}{}".format(sys.path[4],os.sep)):
        if browser in i:
            return True
    return False


def processOpened(browser): # Verific daca webdriver este in lista proceselor ce ruleaza
    return browser in os.popen('wmic process get description').read()


def browserLaunch(browser,*path):
    if "firefox" in browser:
        return webdriver.Firefox()

    if "chrome" in browser:
        return webdriver.Chrome()

    if "edge" in browser:
        return webdriver.Edge() # webdriver-ul noului edge e ciudat...


if __name__=='__main__': # Testing space

    def login(browser):
        driver = browserLaunch(browser)
        driver.implicitly_wait(10)
        driver.get("https://figshare.com/")

        driver.find_element_by_xpath('//a[contains(@href,"https://figshare.com/account/login")]').click()

        driver.find_element_by_xpath('//input[contains(@autocomplete,"email")]').send_keys("bqk79730@yuoia.com")

        driver.find_element_by_xpath('//input[contains(@autocomplete,"password")]').send_keys("Bqk79730@yuoia.com")

        driver.find_element_by_xpath('//button[contains(@type,"submit")]').click()


        #print(driver.find_element_by_xpath('//span[text()="Invalid credentials"]').is_displayed())
        #driver.close()

    #login("edge")
    #print(os.path.isfile(os.path.realpath('../../test.txt')))
    print("fixture.browser.chrome".split(".")[2])
