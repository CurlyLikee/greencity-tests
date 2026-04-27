"""
events_page.py — Page Object for the GreenCity Events page.
URL: https://www.greencity.cx.ua/#/greenCity/events
"""
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.components.event_card_component import EventCardComponent


class EventsPage(BasePage):
    """Page Object for /greenCity/events — events listing page."""

    URL = "https://www.greencity.cx.ua/#/greenCity/events"

    # Locators
    MAIN_HEADER = (By.XPATH, "//p[contains(@class, 'main-header')]")
    ITEMS_FOUND_LABEL = (By.XPATH, "//div[@class='active-filter-container']/p")

    # Event cards (multiple selectors for robustness)
    CARD_SELECTORS = [
        "app-event-card",
        ".event-card",
        ".events-item",
        ".eco-events-list-item",
        "mat-card",
    ]

    FILTER_BUTTONS = (
        By.CSS_SELECTOR,
        "app-tag .tag-block, .tags-list button, .filter-btn, mat-button-toggle button",
    )

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "input[type='search'], input[placeholder*='earch'], .search-input input",
    )

    NO_RESULTS_INDICATOR = (
        By.CSS_SELECTOR,
        ".no-events, .empty-state, .not-found, [class*='no-result']",
    )

    # Constructor
    def __init__(self, driver, timeout=15):
        super().__init__(driver, timeout)

    # Open page
    def open(self):
        """Navigate directly to the Events page."""
        self.driver.get(self.URL)
        return self

    # Header
    def get_main_header(self):
        return self._find(self.MAIN_HEADER)

    # Items count
    def get_items_found_element(self):
        return self._find(self.ITEMS_FOUND_LABEL)

    def get_items_count(self) -> int:
        """Parse the numeric count from the 'N items found' label."""
        text = self.get_items_found_element().text
        match = re.search(r"\d+", text)
        return int(match.group()) if match else 0

    # Event cards
    def get_event_card_elements(self) -> list:
        """Wait and return raw WebElements for event cards.
        Tries several CSS selectors for robustness.
        """
        for selector in self.CARD_SELECTORS:
            try:
                cards = self.wait.until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, selector)
                    )
                )
                if cards:
                    return cards
            except Exception:
                continue
        return []

    def get_cards(self) -> list[EventCardComponent]:
        """Return event cards wrapped as EventCardComponent objects."""
        elements = self.get_event_card_elements()
        return [EventCardComponent(el) for el in elements]

    def get_card_count(self) -> int:
        """Return the number of visible event card elements."""
        return len(self.get_event_card_elements())

    # Filters
    def get_filter_buttons(self) -> list:
        """Return all filter/category buttons."""
        return self._find_all(self.FILTER_BUTTONS)

    def click_filter(self, index: int = 0):
        """Click a filter button by its index."""
        buttons = self.get_filter_buttons()
        button = buttons[index]
        label = button.text.strip()
        button.click()
        return label

    # Search
    def get_search_input(self):
        """Return the search input element (waits until clickable)."""
        return self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))

    def search(self, query: str):
        """Type a search query and submit it."""
        search_input = self.get_search_input()
        search_input.clear()
        search_input.send_keys(query)
        search_input.submit()

    def has_no_results(self) -> bool:
        """Return True if a 'no results' indicator is visible on the page."""
        indicators = self.driver.find_elements(*self.NO_RESULTS_INDICATOR)
        return len(indicators) > 0

    def get_visible_card_count(self) -> int:
        """Return the number of cards currently in the DOM (no waiting)."""
        for selector in self.CARD_SELECTORS:
            cards = self.driver.find_elements(By.CSS_SELECTOR, selector)
            if cards:
                return len(cards)
        return 0

    # Page title checks
    def wait_for_title(self):
        """Wait until the page title is not empty (Angular app initialized)."""
        self.wait.until(lambda d: d.title != "")
        return self.driver.title
