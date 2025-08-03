import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

try:

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_url = f"file://{os.path.join(base_dir, 'dz.html')}"
    driver.get(file_url)

    # 1st frame check
    driver.switch_to.frame("frame1")
    input1 = driver.find_element(By.ID, "input1")
    input1.send_keys("Frame1_Secret")
    verify_btn1 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
    verify_btn1.click()

    # work with alert
    alert = driver.switch_to.alert
    text1 = alert.text
    assert text1 == "Верифікація пройшла успішно!", f"Unexpected alert in frame1: {text1}"
    alert.accept()

    # back to main doc
    driver.switch_to.default_content()

    # 2nd frame check
    driver.switch_to.frame("frame2")
    input2 = driver.find_element(By.ID, "input2")
    input2.send_keys("Frame2_Secret")
    verify_btn2 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
    verify_btn2.click()

    # work with alertм
    alert = driver.switch_to.alert
    text2 = alert.text
    assert text2 == "Верифікація пройшла успішно!", f"Unexpected alert in frame2: {text2}"
    alert.accept()

    # back to main doc
    driver.switch_to.default_content()

    print("Passed ✅")

finally:

    time.sleep(1)
    driver.quit()
