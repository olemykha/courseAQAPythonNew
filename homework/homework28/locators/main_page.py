from selenium.webdriver.common.by import By


class MainPageLocators:
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign In')]")
    SIGN_UP_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign up')]")
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Registration']")
