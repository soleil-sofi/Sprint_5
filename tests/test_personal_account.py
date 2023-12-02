import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data_for_tests import config
from data_for_tests import const
from data_for_tests import locators as loc


def log_in(driver):
    driver.find_element(*loc.FIELD_EMAIL_LOG_IN).send_keys(config.login)
    driver.find_element(*loc.FIELD_PASSWORD_LOG_IN).send_keys(config.password)
    driver.find_element(*loc.BUTTON_LOG_PAGE).click()


@pytest.mark.parametrize("button, start_url", [(loc.BUTTON_LOG_IN_MAIN_PAGE, const.base_url),
                                               (loc.BUTTON_ACCOUNT, const.base_url),
                                               (loc.LINK_LOG_IN, const.register_page),
                                               (loc.LINK_LOG_IN, const.forgot_password_page)])
def test_log_in_main_page(button, start_url):
    driver = webdriver.Chrome()
    driver.get(start_url)
    button_from_params = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(button))
    button_from_params.click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.HEADER_LOGIN_PAGE))
    assert driver.current_url == const.login_page  # проверка перехода на страницу входа
    log_in(driver)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.HEADER_MAIN_PAGE))
    assert driver.current_url == const.base_url
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'
    driver.quit()


@pytest.mark.parametrize("button", [loc.BUTTON_CONSTRUCTOR, loc.LINK_LOGO])
def test_go_to_constructor_and_logo(button):
    driver = webdriver.Chrome()
    driver.get(const.login_page)
    log_in(driver)
    driver.find_element(*loc.BUTTON_ACCOUNT).click()
    button_from_params = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(button))
    button_from_params.click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.HEADER_MAIN_PAGE))
    assert driver.current_url == const.base_url
    driver.quit()


def test_go_to_pa_and_exist():
    driver = webdriver.Chrome()
    driver.get(const.login_page)
    log_in(driver)
    button_account = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.BUTTON_ACCOUNT))
    button_account.click()
    logout_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.BUTTON_LOGOUT))
    logout_button.click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.HEADER_LOGIN_PAGE))
    assert driver.current_url == const.login_page
    driver.quit()




