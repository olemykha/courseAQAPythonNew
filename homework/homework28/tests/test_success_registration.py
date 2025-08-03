from homework.homework28.locators.main_page_for_authorized import MainPageLocatorsForAuthorized
from homework.homework28.wait_utils import wait_for_visibility


def test_successful_registration(driver, open_registration_form, register_user, generate_unique_email, test_password):
    email = generate_unique_email

    register_user(
        name="AutoTest",
        lastname="AutoUser",
        email=email,
        password=test_password,
        repassword=test_password,
        submit=True
    )

    log_out_button = wait_for_visibility(driver, MainPageLocatorsForAuthorized.LOGOUT_BUTTON)
    assert log_out_button.is_displayed()
