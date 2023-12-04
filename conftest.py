import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data_for_tests import const, config, locators as loc


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def log_in(driver):
    driver.get(const.login_page)
    driver.find_element(*loc.FIELD_EMAIL_LOG_IN).send_keys(config.login)
    driver.find_element(*loc.FIELD_PASSWORD_LOG_IN).send_keys(config.password)
    driver.find_element(*loc.BUTTON_LOG_PAGE).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.HEADER_MAIN_PAGE))
    return driver
