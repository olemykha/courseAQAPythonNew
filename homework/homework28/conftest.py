import pytest
import random
import string
from selenium import webdriver
from homework.homework28.locators.main_page import MainPageLocators
from homework.homework28.locators.registration_page import RegistrationPageLocators
from homework.homework28.wait_utils import wait_for_clickable, wait_for_visibility


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def refresh_before_each_test(driver):
    driver.get("https://qauto2.forstudy.space")


def generate_email():
    return "test_user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@gmail.com"


@pytest.fixture
def generate_unique_email():
    return generate_email()


@pytest.fixture
def test_password():
    return "Strong:)Pass123"


@pytest.fixture
def open_registration_form(driver):
    wait_for_clickable(driver, MainPageLocators.SIGN_IN_BUTTON).click()
    wait_for_clickable(driver, MainPageLocators.REGISTRATION_BUTTON).click()


@pytest.fixture
def register_user(driver):
    def _register(name="", lastname="", email="", password="", repassword="", submit=True):
        if name:
            wait_for_visibility(driver, RegistrationPageLocators.NAME_INPUT).send_keys(name)
        if lastname:
            wait_for_visibility(driver, RegistrationPageLocators.LASTNAME_INPUT).send_keys(lastname)
        if email:
            wait_for_visibility(driver, RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        if password:
            wait_for_visibility(driver, RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        if repassword:
            wait_for_visibility(driver, RegistrationPageLocators.REPASSWORD_INPUT).send_keys(repassword)
        if submit:
            wait_for_clickable(driver, RegistrationPageLocators.REGISTER_BUTTON).click()

    return _register
