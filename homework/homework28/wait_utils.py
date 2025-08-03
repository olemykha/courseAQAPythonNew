from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

DEFAULT_TIMEOUT = 3


def wait_for_visibility(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        ec.visibility_of_element_located(locator)
    )


def wait_for_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        ec.element_to_be_clickable(locator)
    )
