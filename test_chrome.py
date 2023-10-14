import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_url="https://www.adidas.com"

@pytest.mark.parametrize("item",
                         [
                             "sneakers",
                             "t-shirts"
                         ])

@pytest.mark.adidas
def test_adidas_search(browser, item):
    browser.get(base_url)
    time.sleep(3)
    browser.find_element(By.ID, "glass-gdpr-default-consent-accept-button").click()
    #COOKIES
    browser.find_element(By.CLASS_NAME, "_input_1f3oz_13").send_keys(item + Keys.ENTER)
    #SEARCH FIELD
    browser.find_element(By.CSS_SELECTOR, "div#filters-panel > div > div > .title___1MG81").click()
    #SEX
    browser.find_element(By.CSS_SELECTOR, "div#filters-panel > div > div .plp-sidebar-item___2cVCo  a[title='Ανδρικά']").click()
    #SEX
    time.sleep(20)
    #because my computer is bad
    browser.find_element(By.CLASS_NAME, "gl-modal__close").click()
    #pop-up window
    browser.find_element(By.CSS_SELECTOR, ".sortby_wrapper___1Lwyk [role='combobox']").click()
    #price-window
    browser.find_element(By.CSS_SELECTOR, "ul#gl-dropdown-custom__listbox--plp-sort-dropdown > li:nth-of-type(4)").click()
    #price
    time.sleep(5)