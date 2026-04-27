"""
filter_panel.py — Filter/tag panel component for GreenCity Events page.
"""
import allure
from selenium.webdriver.common.by import By

from src.components.base_component import BaseComponent


class FilterPanel(BaseComponent):
    """Filter panel component — tag/category filter buttons."""

    # Locators (relative to filter container root)
    FILTER_BUTTONS = (
        By.CSS_SELECTOR,
        ".tag-block, button, mat-button-toggle button",
    )

    @allure.step("Get all filter buttons")
    def get_buttons(self) -> list:
        """Return all filter/tag button elements."""
        return self.find_elements(*self.FILTER_BUTTONS)

    @allure.step("Click filter at index {index}")
    def click_filter(self, index: int = 0) -> str:
        """Click a filter button by index. Returns the filter label text."""
        buttons = self.get_buttons()
        button = buttons[index]
        label = button.text.strip()
        button.click()
        return label

    def get_count(self) -> int:
        """Return the number of available filter buttons."""
        return len(self.get_buttons())
