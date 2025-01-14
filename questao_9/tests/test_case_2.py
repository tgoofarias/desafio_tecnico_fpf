import time
import random

import pytest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


URL = "https://www.vanilton.net/triangulo/"

def test_case_2(driver):
    # Test Case 2: Verify Isosceles Triangle
    # Step 1: Fill the V1 and V2 inputs with the same positive number
    driver.get(URL)

    number = random.randint(1, 100)
    for i in range(1, 3):
        input = driver.find_element(By.NAME, f"V{i}")
        input.send_keys(number)

    # Step 2: Fill the V3 input with a different positive number that is lower than the sum of the other two sides
    number = random.randint(1, number)
    input = driver.find_element(By.NAME, "V3")
    input.send_keys(number)

    driver.find_element(By.XPATH, '//input[@value="Identificar"]').click()

    time.sleep(1)

    try:
        div_result = driver.find_element(By.XPATH, "//img").find_element(By.XPATH, "..")
    except NoSuchElementException as e:
        raise AssertionError("The program didn't show a result") from e

    assert div_result.text == "Isósceles", f"The program gave a wrong result: {div_result.text}"
