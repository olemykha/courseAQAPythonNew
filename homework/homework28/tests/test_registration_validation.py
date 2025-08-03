import pytest
from homework.homework28.locators.registration_page import RegistrationPageLocators
from homework.homework28.wait_utils import wait_for_visibility, wait_for_clickable


@pytest.mark.parametrize("data, error_locator, expected_error", [
    (
        {
            "name": "AutoTest",
            "lastname": "Negative",
            "email": "notanemail",
            "password": "Test1234",
            "repassword": "Test1234"
        },
        RegistrationPageLocators.EMAIL_ERROR_INVALID, "Email is incorrect"
    ),
    (
        {
            "name": "1",
            "lastname": "Negative",
            "email": "conflict_user@mail.com",
            "password": "Test1234",
            "repassword": "Mismatch123"
        },
        RegistrationPageLocators.NAME_ERROR_INVALID, "Name is invalid"
    ),
    (
        {
            "name": "AutoTest",
            "lastname": "1",
            "email": "conflict_user@mail.com",
            "password": "Test1234",
            "repassword": "Mismatch123"
        },
        RegistrationPageLocators.LAST_NAME_ERROR_INVALID, "Last name is invalid"
    ),
])
def test_negative_field_validation(driver, open_registration_form, register_user,
                                   data, error_locator, expected_error):
    register_user(**data, submit=False)
    error_element = wait_for_visibility(driver, error_locator)
    assert error_element.text.strip() == expected_error


@pytest.mark.parametrize("field_to_clear, field_locator, error_locator, expected_error", [
    ("name", RegistrationPageLocators.NAME_INPUT, RegistrationPageLocators.NAME_ERROR,
     "Name required"),
    ("lastname", RegistrationPageLocators.LASTNAME_INPUT, RegistrationPageLocators.LASTNAME_ERROR,
     "Last name required"),
    ("email", RegistrationPageLocators.EMAIL_INPUT, RegistrationPageLocators.EMAIL_ERROR,
     "Email required"),
    ("password", RegistrationPageLocators.PASSWORD_INPUT, RegistrationPageLocators.PASSWORD_ERROR,
     "Password required"),
    ("repassword", RegistrationPageLocators.REPASSWORD_INPUT, RegistrationPageLocators.REPASSWORD_ERROR,
     "Re-enter password required"),
])
def test_empty_field_validation(driver,
                                open_registration_form,
                                field_to_clear,
                                field_locator,
                                error_locator,
                                expected_error):

    valid_data = {"name": "Test", "lastname": "User", "email": "test@example.com", "password": "Password123",
                  "repassword": "Password123", field_to_clear: ""}

    for key, value in valid_data.items():
        if value:
            field = wait_for_visibility(driver, getattr(RegistrationPageLocators, f"{key.upper()}_INPUT"))
            field.send_keys(value)

    target_field = wait_for_visibility(driver, field_locator)
    target_field.click()

    if field_to_clear == "email":
        other_field = wait_for_visibility(driver, RegistrationPageLocators.PASSWORD_INPUT)
        other_field.click()
    else:
        wait_for_clickable(driver, RegistrationPageLocators.MODAL_BODY).click()

    error_element = wait_for_visibility(driver, error_locator)
    assert error_element.text.strip() == expected_error, \
        f"Expected: '{expected_error}', but got: '{error_element.text.strip()}'"
