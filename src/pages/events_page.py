"""
events_page.py — Page Object for the GreenCity Events page.
URL: https://www.greencity.cx.ua/#/greenCity/events
"""
import re

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage
from src.components.header import Header
from src.components.filter_panel import FilterPanel
from src.components.event_card import EventCard


class EventsPage(BasePage):
    """Page Object for /greenCity/events — events listing page."""

    URL = "https://www.greencity.cx.ua/#/greenCity/events"

    # Locators — component roots
    HEADER_ROOT = (By.CSS_SELECTOR, "header, app-header")
    FILTER_CONTAINER = (
        By.CSS_SELECTOR,
        "app-tag, .tags-list, .filter-container, mat-button-toggle-group",
    )

    # Page-specific locators
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

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "input[type='search'], input[placeholder*='earch'], .search-input input",
    )
    NO_RESULTS_INDICATOR = (
        By.CSS_SELECTOR,
        ".no-events, .empty-state, .not-found, [class*='no-result']",
    )

    # Components (lazy-loaded)
    @allure.step("Get Header component")
    def get_header(self) -> Header:
        """Return the Header component."""
        root = self._find(self.HEADER_ROOT)
        return Header(root)

    @allure.step("Get FilterPanel component")
    def get_filter_panel(self) -> FilterPanel:
        """Return the FilterPanel component."""
        root = self._find(self.FILTER_CONTAINER)
        return FilterPanel(root)

    # Open page
    @allure.step("Open Events page")
    def open(self):
        """Navigate directly to the Events page."""
        self.driver.get(self.URL)
        return self

    # Header
    @allure.step("Get main page header text")
    def get_main_header(self):
        return self._find(self.MAIN_HEADER)

    # Items count
    @allure.step("Get items found count")
    def get_items_count(self) -> int:
        """Parse the numeric count from the 'N items found' label."""
        text = self._find(self.ITEMS_FOUND_LABEL).text
        match = re.search(r"\d+", text)
        return int(match.group()) if match else 0

    # Event cards
    @allure.step("Wait for event cards to load")
    def get_event_card_elements(self) -> list:
        """Wait and return raw WebElements for event cards."""
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

    @allure.step("Get event cards as EventCard components")
    def get_cards(self) -> list[EventCard]:
        """Return event cards wrapped as EventCard component objects."""
        elements = self.get_event_card_elements()
        return [EventCard(el) for el in elements]

    @allure.step("Get number of visible event cards")
    def get_card_count(self) -> int:
        """Return the number of visible event card elements."""
        return len(self.get_event_card_elements())

    # Search
    @allure.step("Enter search query: '{query}'")
    def search(self, query: str):
        """Type a search query and submit it."""
        search_input = self._wait_clickable(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(query)
        search_input.submit()

    @allure.step("Check if 'no results' indicator is visible")
    def has_no_results(self) -> bool:
        """Return True if a 'no results' indicator is visible on the page."""
        indicators = self.driver.find_elements(*self.NO_RESULTS_INDICATOR)
        return len(indicators) > 0

    @allure.step("Get count of cards currently in DOM (no wait)")
    def get_visible_card_count(self) -> int:
        """Return the number of cards currently in the DOM (no waiting)."""
        for selector in self.CARD_SELECTORS:
            cards = self.driver.find_elements(By.CSS_SELECTOR, selector)
            if cards:
                return len(cards)
        return 0

    # Page title
    @allure.step("Wait for page title to appear")
    def wait_for_title(self) -> str:
        """Wait until the page title is not empty (Angular app initialized)."""
        self.wait.until(lambda d: d.title != "")
        return self.driver.title

    @allure.step("Wait for search results to update")
    def wait_for_search_results(self):
        """Wait until cards disappear or no-results indicator appears."""
        self.wait.until(
            lambda d: (
                len(d.find_elements(By.CSS_SELECTOR, ", ".join(self.CARD_SELECTORS))) == 0
                or len(d.find_elements(*self.NO_RESULTS_INDICATOR)) > 0
            )
        )

    @allure.step("Wait for event cards to reload after filter")
    def wait_for_cards_reload(self, old_cards: list):
        """Wait until at least one old card becomes stale (page refreshed)."""
        if old_cards:
            try:
                self.wait.until(EC.staleness_of(old_cards[0]))
            except Exception:
                pass
        return self.get_event_card_elements()
