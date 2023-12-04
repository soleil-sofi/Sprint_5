import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data_for_tests import const, functions as func, locators as loc


class TestRegistration:
    @staticmethod
    def registration(driver, name, password, email):
        driver.find_element(*loc.FIELD_NAME_REGISTRATION).send_keys(name)
        driver.find_element(*loc.FIELD_EMAIL_REGISTRATION).send_keys(email)
        driver.find_element(*loc.FIELD_PASSWORD_REGISTRATION).send_keys(password)
        driver.find_element(*loc.BUTTON_REGISTRATION).click()

    def test_auth_correct_data(self, driver):
        name = 'test'
        password = func.generate_password(max_length=6, min_length=6)
        email = func.generate_email()
        driver.get(const.register_page)
        self.registration(driver, name, password, email)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc.HEADER_LOGIN_PAGE))
        assert driver.current_url == const.login_page

    def test_auth_invalid_password(self, driver):
        driver.get(const.register_page)
        self.registration(driver, 'test', func.generate_password(max_length=5), func.generate_email())
        assert driver.current_url == const.register_page
        driver.find_element(By.XPATH, './/main').click()
        assert expected_conditions.visibility_of_element_located(loc.MSG_PASSWORD_ERROR) is not False

    @pytest.mark.parametrize("email", ['test', 'test@test', 'test.test'])
    def test_auth_invalid_email(self, email, driver):
        driver.get(const.register_page)
        self.registration(driver, 'test', func.generate_password(min_length=6), email)
        assert driver.current_url == const.register_page
        assert expected_conditions.visibility_of_element_located(loc.MSG_EMAIL_ERROR) is not False

    def test_auth_empty_name(self, driver):
        driver.get(const.register_page)
        self.registration(driver, 'test', func.generate_password(max_length=5), func.generate_email())
        assert driver.current_url == const.register_page
