"""
test_events_page.py — Automated UI tests for the GreenCity Events page.
Refactored to use Page Object Pattern (PO).
"""
import unittest
import time

from utils import get_driver
from pages.events_page import EventsPage


class EventsPageTests(unittest.TestCase):
    """Tests for https://www.greencity.cx.ua/#/greenCity/events"""

    def setUp(self):
        self.driver = get_driver()
        self.events_page = EventsPage(self.driver)
        self.events_page.open()

    def tearDown(self):
        self.driver.quit()

    # TC-01: Events list is displayed on page load
    def test_events_list_is_displayed_on_page_load(self):
        """TC-01: Events list is visible after opening the Events page."""
        cards = self.events_page.get_event_card_elements()

        self.assertGreater(
            len(cards), 0,
            "Expected at least one event card on the page, but found none.",
        )

    # TC-02: Filter by category updates the displayed events
    def test_filter_by_category_updates_list(self):
        """TC-02: Clicking a category filter changes the displayed events."""
        # Wait for initial load
        self.events_page.get_event_card_elements()

        # Get filter buttons and click the first one
        filter_buttons = self.events_page.get_filter_buttons()
        self.assertGreater(len(filter_buttons), 0, "No filter buttons found on the page.")

        filter_label = self.events_page.click_filter(0)

        # Wait for the list to refresh, then check cards
        time.sleep(2)
        updated_cards = self.events_page.get_event_card_elements()

        self.assertGreater(
            len(updated_cards), 0,
            f"After clicking filter '{filter_label}', no events are displayed.",
        )

    # TC-03: Clicking an event opens its detail page
    def test_click_event_opens_detail_page(self):
        """TC-03: Clicking an event card navigates to the event detail page."""
        cards = self.events_page.get_cards()
        self.assertGreater(len(cards), 0, "No event cards found to click.")

        url_before = self.events_page.get_current_url()

        # Click the first card's title link
        cards[0].click_title()

        # Wait for navigation
        self.events_page.wait.until(
            lambda d: d.current_url != url_before
        )

        url_after = self.events_page.get_current_url()
        self.assertNotEqual(url_before, url_after, "URL did not change after clicking an event card.")
        self.assertIn("event", url_after.lower(), "New URL does not look like an event detail page.")

    # TC-04 (Negative): Search with no matching query shows empty state
    def test_search_with_no_results_shows_empty_state(self):
        """TC-04 (Negative): A nonsense search query returns no events and shows a message."""
        # Wait for page to load fully
        self.events_page.get_event_card_elements()

        # Perform a search that should match nothing
        self.events_page.search("xyzxyzxyz999")

        # Wait for results to update
        time.sleep(2)

        visible_cards = self.events_page.get_visible_card_count()
        no_results = self.events_page.has_no_results()

        self.assertTrue(
            visible_cards == 0 or no_results,
            "Expected no results or an empty-state message, but event cards are still displayed.",
        )

    # TC-05 (Negative): Page title is correct (smoke check)
    def test_page_title_is_not_empty(self):
        """TC-05 (Negative/Smoke): The page has a non-empty title (basic load check)."""
        title = self.events_page.wait_for_title()

        self.assertTrue(len(title) > 0, "Page title is empty — the page may have failed to load.")
        self.assertNotIn("404", title, "Page title contains '404' — page not found.")
        self.assertNotIn("Error", title, "Page title contains 'Error'.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
