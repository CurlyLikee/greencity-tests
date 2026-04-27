"""
event_card.py — Single event card component for GreenCity Events page.
"""
import allure
from selenium.webdriver.common.by import By

from src.components.base_component import BaseComponent


class EventCard(BaseComponent):
    """Represents a single event card on the Events page."""

    # Locators (scoped to the card root)
    NAME = (By.XPATH, ".//p[contains(@class, 'event-name')]")
    TITLE_LINK = (By.CSS_SELECTOR, "a, h2, h3, .event-title")
    MORE_BUTTON = (
        By.XPATH,
        ".//button[normalize-space()='More' or normalize-space()='Більше']",
    )

    @allure.step("Get event card name")
    def get_name(self) -> str:
        """Return the visible event name text."""
        return self.find_element(*self.NAME).text

    @allure.step("Click event card title")
    def click_title(self):
        """Click the event title/link to open the detail page."""
        try:
            self.find_element(*self.TITLE_LINK).click()
        except Exception:
            self.node.click()

    @allure.step("Click 'More' button on event card")
    def click_more(self):
        """Click the 'More' / 'Більше' button on the card."""
        self.find_element(*self.MORE_BUTTON).click()
