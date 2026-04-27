"""
base_component.py — Base class for reusable UI components.
A component wraps a root WebElement and searches within it.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BaseComponent:
    """Base component — scopes find_element calls to the root node."""

    def __init__(self, root: WebElement):
        self.node = root
        self.driver = root.parent  # underlying WebDriver instance

    def find_element(self, by=By.XPATH, value=None):
        """Find a child element inside this component's root."""
        return self.node.find_element(by, value)

    def find_elements(self, by=By.XPATH, value=None):
        """Find all matching child elements inside this component's root."""
        return self.node.find_elements(by, value)
