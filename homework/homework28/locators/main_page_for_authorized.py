from selenium.webdriver.common.by import By


class MainPageLocatorsForAuthorized:
    LOGOUT_BUTTON = (By.XPATH, "//a[span[contains(@class, 'icon-logout')] and contains(text(), 'Log out')]")
