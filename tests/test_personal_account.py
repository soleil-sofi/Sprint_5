import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data_for_tests import config
from data_for_tests import const
from data_for_tests import locators as loc


class TestPersonalAccount:
    @staticmethod
    def log_in(driver):
        driver.find_element(*loc.FIELD_EMAIL_LOG_IN).send_keys(config.login)
        driver.find_element(*loc.FIELD_PASSWORD_LOG_IN).send_keys(config.password)
        driver.find_element(*loc.BUTTON_LOG_PAGE).click()

    @pytest.mark.parametrize("button, start_url", [(loc.BUTTON_LOG_IN_MAIN_PAGE, const.base_url),
                                                   (loc.BUTTON_ACCOUNT, const.base_url),
                                                   (loc.LINK_LOG_IN, const.register_page),
                                                   (loc.LINK_LOG_IN, const.forgot_password_page)])
    def test_log_in_main_page(self, button, start_url, driver):
        driver.get(start_url)
        button_from_params = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(button))
        button_from_params.click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.HEADER_LOGIN_PAGE))
        assert driver.current_url == const.login_page
        self.log_in(driver)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.HEADER_MAIN_PAGE))
        assert driver.current_url == const.base_url
        assert expected_conditions.visibility_of_element_located(loc.BUTTON_ORDER) is not False

    @pytest.mark.parametrize("button", [loc.BUTTON_CONSTRUCTOR, loc.LINK_LOGO])
    def test_go_to_constructor_and_logo(self, button, driver):
        driver.get(const.login_page)
        self.log_in(driver)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.HEADER_MAIN_PAGE))
        driver.find_element(*loc.BUTTON_ACCOUNT).click()
        button_from_params = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(button))
        button_from_params.click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.HEADER_MAIN_PAGE))
        assert driver.current_url == const.base_url

    def test_go_to_pa_and_exist(self, driver):
        driver.get(const.login_page)
        self.log_in(driver)
        button_account = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.BUTTON_ACCOUNT))
        button_account.click()
        logout_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.BUTTON_LOGOUT))
        logout_button.click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.HEADER_LOGIN_PAGE))
        assert driver.current_url == const.login_page




