import random
import string


def generate_email():
    login = ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for _ in range(6))
    domain = random.choice(['ya.ru', 'yandex.ru', 'mail.ru', 'gmail.com'])

    email = login + '@' + domain
    return email


def generate_password(min_length=1, max_length=10):
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for _ in range(length))
