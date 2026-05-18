import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def  browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
def test_open_s1(browser):
    browser.get('https://old.yummyani.me/catalog/top?ysclid=mp1lakdrts393435569')
    elements1 = browser.find_element(By.XPATH,  '//a[text()="Монолог фармацевта 2"]')
    elements1.click()
    assert elements1.text == 'Монолог фармацевта 2'
