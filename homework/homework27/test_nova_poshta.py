import pytest
from selenium import webdriver
from homework.homework27.np_tracker import NPTracker


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_parcel_status_for_non_existent_number(driver):
    tracker = NPTracker(driver)
    tracking_number = "20450257913697"
    expected_status = "Ми не знайшли посилку за таким номером."

    tracker.open_page()
    tracker.enter_tracking_number(tracking_number)
    actual_status = tracker.get_parcel_error_status()

    assert expected_status in actual_status, (
        f"Expected text that contains '{expected_status}', but get: '{actual_status}'"
    )
