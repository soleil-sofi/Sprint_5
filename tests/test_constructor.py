from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data_for_tests import locators as loc
from data_for_tests import const


def test_go_to_sauces():
    driver = webdriver.Chrome()
    driver.get(const.base_url)
    sauces_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(loc.BUTTON_SAUCES))
    sauces_button.click()
    assert 'current' in driver.find_element(*loc.BUTTON_SAUCES).get_attribute('class')
    driver.quit()


def test_go_to_fillings():
    driver = webdriver.Chrome()
    driver.get(const.base_url)
    fillings_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(loc.BUTTON_FILLINGS))
    fillings_button.click()
    assert 'current' in driver.find_element(*loc.BUTTON_FILLINGS).get_attribute('class')
    driver.quit()


def test_go_to_buns():
    driver = webdriver.Chrome()
    driver.get(const.base_url)
    sauces_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(loc.BUTTON_SAUCES))
    sauces_button.click()  # сначала переход к соусам, так как по дефолту булки видны сразу при открытии страницы
    buns_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(loc.BUTTON_BUNS))
    buns_button.click()
    assert 'current' in driver.find_element(*loc.BUTTON_BUNS).get_attribute('class')
    driver.quit()
