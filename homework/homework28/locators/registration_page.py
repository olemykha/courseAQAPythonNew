from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    MODAL_BODY = (By.XPATH, "//div[@class='modal-body']")
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    LASTNAME_INPUT = (By.XPATH, "//input[@name='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    REPASSWORD_INPUT = (By.XPATH, "//input[@name='repeatPassword']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Register')]")
    EMAIL_ERROR_INVALID = (By.XPATH, "//p[contains(text(), 'Email is incorrect')]")
    NAME_ERROR_INVALID = (By.XPATH, "//p[contains(text(), 'Name is invalid')]")
    LAST_NAME_ERROR_INVALID = (By.XPATH, "//p[contains(text(), 'Last name is invalid')]")
    REPASSWORD_ERROR_MATCH = (By.XPATH, "//p[contains(text(), 'Passwords do not match')]")
    USER_EXISTS_ERROR = (By.XPATH, "//p[contains(@class, 'alert-danger') and text()='User already exists']")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[@aria-label='Close']")
    EMAIL_ERROR = (By.XPATH, "//p[text()='Email required']")
    NAME_ERROR = (By.XPATH,
                  "//div[contains(@class, 'invalid-feedback')]/p[text()='Name required']")
    LASTNAME_ERROR = (By.XPATH,
                      "//div[contains(@class, 'invalid-feedback')]/p[text()='Last name required']")
    PASSWORD_ERROR = (By.XPATH,
                      "//div[contains(@class, 'invalid-feedback')]/p[text()='Password required']")
    REPASSWORD_ERROR = (By.XPATH,
                        "//div[contains(@class, 'invalid-feedback')]/p[text()='Re-enter password required']")
