import time
import random

import pytest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


URL = "https://www.vanilton.net/triangulo/"

def test_case_4(driver):
    # Test Case 4: Verify Scalene Triangle
    # Step 1: Fill the V1, V2 and V3 inputs with three different positive number which 
    # one of them should be greater then the sum of the other two numbers (e.g 4, 5, 10)
    driver.get(URL)

    number = random.randint(1, 100)
    for i in range(1, 3):
        input = driver.find_element(By.NAME, f"V{i}")
        input.send_keys(number)

    input = driver.find_element(By.NAME, "V3")
    input.send_keys(number * 3)

    driver.find_element(By.XPATH, '//input[@value="Identificar"]').click()

    time.sleep(1)

    try:
        driver.find_element(By.XPATH, "//img")
        raise AssertionError("The program gave a result to a invalid operation")
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, "errorMessage")
    except NoSuchElementException:
        raise AssertionError("The program didn't show an error message when passed a invalid input")
