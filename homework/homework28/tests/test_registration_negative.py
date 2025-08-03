from homework.homework28.locators.main_page_for_authorized import MainPageLocatorsForAuthorized
from homework.homework28.wait_utils import wait_for_visibility, wait_for_clickable
from homework.homework28.locators.registration_page import RegistrationPageLocators
from homework.homework28.locators.main_page import MainPageLocators


def test_negative_pass_mismatch(driver, open_registration_form, register_user):
    register_user(
        name="AutoTest",
        lastname="Mismatch",
        email="mismatch_user@mail.com",
        password="Test1234",
        repassword="Wrong1234",
        submit=False
    )

    wait_for_clickable(driver, RegistrationPageLocators.MODAL_BODY).click()
    error_element = wait_for_visibility(driver, RegistrationPageLocators.REPASSWORD_ERROR_MATCH)
    assert error_element.text.strip() == "Passwords do not match"


def test_existing_user_registration(driver, open_registration_form, register_user, generate_unique_email, test_password):
    email = generate_unique_email

    register_user(
        name="Alex",
        lastname="Smith",
        email=email,
        password=test_password,
        repassword=test_password,
        submit=True
    )
    wait_for_clickable(driver, MainPageLocatorsForAuthorized.LOGOUT_BUTTON).click()
    wait_for_clickable(driver, MainPageLocators.SIGN_IN_BUTTON).click()
    wait_for_clickable(driver, MainPageLocators.REGISTRATION_BUTTON).click()
    wait_for_visibility(driver, RegistrationPageLocators.NAME_INPUT)

    register_user(
        name="Alex",
        lastname="Smith",
        email=email,
        password=test_password,
        repassword=test_password
    )

    wait_for_clickable(driver, RegistrationPageLocators.MODAL_BODY).click()
    error_element = wait_for_visibility(driver, RegistrationPageLocators.USER_EXISTS_ERROR)
    assert error_element.text.strip() == "User already exists", \
        f"Expected error message 'User already exists', but got: '{error_element.text.strip()}'"
