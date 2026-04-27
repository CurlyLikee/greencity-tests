"""
event_card_component.py — Page component for a single event card.
"""
from selenium.webdriver.common.by import By

from pages.components.base_component import BaseComponent


class EventCardComponent(BaseComponent):
    """Represents a single event card on the Events page."""

    # Locators (scoped to the card root)
    NAME = (By.XPATH, ".//p[contains(@class, 'event-name')]")
    TITLE_LINK = (By.CSS_SELECTOR, "a, h2, h3, .event-title")
    MORE_BUTTON = (
        By.XPATH,
        ".//button[normalize-space()='More' or normalize-space()='Більше']",
    )

    # Actions
    def get_name(self) -> str:
        """Return the visible event name text."""
        return self.find_element(*self.NAME).text

    def click_title(self):
        """Click the event title / link to open the detail page."""
        try:
            self.find_element(*self.TITLE_LINK).click()
        except Exception:
            self.node.click()

    def click_more(self):
        """Click the 'More' / 'Більше' button on the card."""
        self.find_element(*self.MORE_BUTTON).click()
