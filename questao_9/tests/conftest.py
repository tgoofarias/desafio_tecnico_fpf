import pytest

from selenium import webdriver

chrome_instance = webdriver.Chrome()


@pytest.fixture
def driver():
    return chrome_instance
