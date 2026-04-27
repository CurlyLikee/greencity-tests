"""
base_component.py — Base class for all reusable UI components.
A component wraps a root WebElement and scopes searches within it.
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseComponent:
    """Base component — scopes find_element calls to the root node."""

    def __init__(self, root: WebElement, timeout: int = 10):
        self.node = root
        self.driver = root.parent
        self.wait = WebDriverWait(self.driver, timeout)

    def find_element(self, by=By.XPATH, value=None):
        """Find a child element inside this component's root."""
        return self.node.find_element(by, value)

    def find_elements(self, by=By.XPATH, value=None):
        """Find all matching child elements inside this component's root."""
        return self.node.find_elements(by, value)

    def is_displayed(self) -> bool:
        """Check if the component root element is visible."""
        return self.node.is_displayed()

    @property
    def text(self) -> str:
        """Return the text content of the component root."""
        return self.node.text
