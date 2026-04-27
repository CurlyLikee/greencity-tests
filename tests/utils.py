"""
utils.py — helper functions for GreenCity UI tests.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver() -> webdriver.Chrome:
    """
    Create and return a configured Chrome WebDriver instance.
    Runs headless by default so tests work in CI and without a display.
    """
    options = Options()
    options.add_argument("--headless")          # run without opening a real browser window
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)                   # fallback implicit wait (seconds)
    return driver
