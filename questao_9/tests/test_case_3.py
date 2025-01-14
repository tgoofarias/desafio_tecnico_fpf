import time
import random

import pytest

from selenium.webdriver.common.by import By


URL = "https://www.vanilton.net/triangulo/"

def test_case_2(driver):
    # Test Case 3: Verify Scalene Triangle
    # Step 1: Fill the V1, V2 and V3 inputs with the three different positive number each that are lower than
    # the sum of the other tow numbers (e.g 3, 4, 5)
    driver.get(URL)

    number = random.randint(1, 100)
    for i in range(1, 4):
        input = driver.find_element(By.NAME, f"V{i}")
        input.send_keys(number + i)

    driver.find_element(By.XPATH, '//input[@value="Identificar"]').click()

    time.sleep(1)

    try:
        div_result = driver.find_element(By.XPATH, "//img").find_element(By.XPATH, "..")
    except Exception as e:
        raise AssertionError("The program didn't show a result") from e

    assert div_result.text == "Escaleno", f"The program gave a wrong result: {div_result.text}"
