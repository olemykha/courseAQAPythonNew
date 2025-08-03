from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class NPTracker:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def open_page(self):
        self.driver.get(self.url)

    def enter_tracking_number(self, tracking_number: str):
        input_field = WebDriverWait(self.driver, 2).until(
            ec.presence_of_element_located((
                By.XPATH,
                "//input[contains(@type, 'text') and contains(@placeholder, 'Номер посилки')]"
            ))
        )
        input_field.send_keys(tracking_number)
        input_field.send_keys(Keys.ENTER)

    def get_parcel_error_status(self) -> str:
        status_element = WebDriverWait(self.driver, 2).until(
            ec.visibility_of_element_located((
                By.XPATH,
                "//div[contains(@id, 'np-number-input-desktop-message-error-message')]"
            ))
        )
        return status_element.text.strip()
