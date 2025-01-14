import time
import random

import pytest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


URL = "https://www.vanilton.net/triangulo/"

def test_case_1(driver):
    # Test Case 1: Verify Equilateral Triangle
    # Step 1: Fill the V1, V2 and V3 input sides with the same positive number
    driver.get(URL)

    number = random.randint(1, 100)
    for i in range(1, 4):
        input = driver.find_element(By.NAME, f"V{i}")
        input.send_keys(number)
    driver.find_element(By.XPATH, '//input[@value="Identificar"]').click()

    time.sleep(1)

    try:
        div_result = driver.find_element(By.XPATH, "//img").find_element(By.XPATH, "..")
    except NoSuchElementException as e:
        raise AssertionError("The program didn't show a result") from e

    assert div_result.text == "Equilátero", f"The program gave a wrong result: {div_result.text}"
