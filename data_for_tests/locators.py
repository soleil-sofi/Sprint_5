from selenium import webdriver
from selenium.webdriver.common.by import By

BUTTON_LOG_IN_MAIN_PAGE = (By.XPATH, './/*[@id="root"]/div/main/section[2]/div/button')
# Кнопка "Войти" на главной странице
FIELD_EMAIL_LOG_IN = (By.NAME, 'name')  # Поле "Email" на странице входа
FIELD_PASSWORD_LOG_IN = (By.NAME, 'Пароль')  # Поле "Пароль" на странице входа
BUTTON_ACCOUNT = (By.XPATH, './/p[text()="Личный Кабинет"]')  # Кнопка ЛК
BUTTON_LOG_PAGE = (By.XPATH, './/*[@id="root"]/div/main/div/form/button')  # Кнопка "Войти" на странице входа
FIELD_NAME_REGISTRATION = (By.XPATH, './/label[text()="Имя"]/following-sibling::input[@name="name"]')
# Поле имени на странице регистрации
FIELD_EMAIL_REGISTRATION = (By.XPATH, './/label[text()="Email"]/following-sibling::input[@name="name"]')
# Поле почты на странице регистрации
FIELD_PASSWORD_REGISTRATION = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@name='Пароль']")
# Поле пароля на странице регистрации
BUTTON_REGISTRATION = (By.XPATH, './/button[text()="Зарегистрироваться"]')  # Кнопка регистрации
LINK_LOG_IN = (By.XPATH, './/a[@href="/login"]')  # Ссылка на страницу входа
MSG_PASSWORD_ERROR = (By.XPATH, '//p[text()="Некорректный пароль"]')  # Сообщение о невалидном пароле
MSG_EMAIL_ERROR = (By.XPATH, './/p[text()="Такой пользователь уже существует"]')  # Сообщение о невалидном логине
HEADER_LOGIN_PAGE = (By.XPATH, './/h2[text()="Вход"]')  # Заголовок на странице входа
HEADER_MAIN_PAGE = (By.XPATH, './/h1[text()="Соберите бургер"]')  # Заголовок на главной странице
BUTTON_LOGOUT = (By.XPATH, './/li[3]/button[text()="Выход"]')  # Кнопка выхода из аккаунта
BUTTON_CONSTRUCTOR = (By.XPATH, './/li[1]/a/p[text()="Конструктор"]')  # Кнопка перехода к контруктору
LINK_LOGO = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a[@href="/"]')  # Кнопка-лого
BUTTON_SAUCES = (By.XPATH, ".//span[contains(text(), 'Соусы')]/parent::div")
BUTTON_BUNS = (By.XPATH, ".//span[contains(text(), 'Булки')]/parent::div")
BUTTON_FILLINGS = (By.XPATH, ".//span[contains(text(), 'Начинки')]/parent::div")
