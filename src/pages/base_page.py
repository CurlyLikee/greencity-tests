"""
base_page.py — Base Page Object for GreenCity.
Contains driver, waits, and generic helper methods.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base page with driver access and explicit wait helpers."""

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Helper: explicit wait wrappers
    def _find(self, locator):
        """Find element with explicit wait (presence)."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def _find_all(self, locator):
        """Find all matching elements with explicit wait."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def _click(self, locator):
        """Wait for element to be clickable, then click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def _wait_clickable(self, locator):
        """Wait for element to be clickable and return it."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def open(self, url):
        """Navigate to a URL."""
        self.driver.get(url)

    def get_current_url(self) -> str:
        """Return the current URL."""
        return self.driver.current_url

    def get_page_title(self) -> str:
        """Return the browser page title."""
        return self.driver.title
