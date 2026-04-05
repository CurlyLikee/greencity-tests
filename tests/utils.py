"""
utils.py — helper functions for GreenCity UI tests.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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


def wait_for_events_to_load(wait) -> list:
    """
    Wait until event cards are present on the page and return them.

    Tries several CSS selectors that GreenCity may use for event cards.
    Returns the first non-empty list found, or an empty list if nothing loads.
    """
    selectors = [
        "app-event-card",
        ".event-card",
        ".events-item",
        ".eco-events-list-item",
    ]

    for selector in selectors:
        try:
            cards = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
            )
            if cards:
                return cards
        except Exception:
            continue

    return []
