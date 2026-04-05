import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils import get_driver, wait_for_events_to_load

EVENTS_URL = "https://www.greencity.cx.ua/#/greenCity/events"


class EventsPageTests(unittest.TestCase):

    # -------------------------------------------------------------------------
    # TC-01: Events list is displayed on page load
    # -------------------------------------------------------------------------
    def setUp(self):
        self.driver = get_driver()
        self.wait = WebDriverWait(self.driver, 15)

    def tearDown(self):
        self.driver.quit()

    def test_events_list_is_displayed_on_page_load(self):
        """TC-01: Events list is visible after opening the Events page."""
        # Precondition: open the events page
        self.driver.get(EVENTS_URL)

        # Wait until at least one event card is present in the DOM
        event_cards = wait_for_events_to_load(self.wait)

        # Assert that the list is not empty
        self.assertGreater(
            len(event_cards), 0,
            "Expected at least one event card on the page, but found none."
        )

    # -------------------------------------------------------------------------
    # TC-02: Filter by category updates the displayed events
    # -------------------------------------------------------------------------
    def test_filter_by_category_updates_list(self):
        """TC-02: Clicking a category filter changes the displayed events."""
        self.driver.get(EVENTS_URL)

        # Wait for the page to load
        wait_for_events_to_load(self.wait)

        # Find the filter/tag buttons
        filter_buttons = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "app-tag .tag-block, .tags-list button, .filter-btn, mat-button-toggle button")
            )
        )

        self.assertGreater(len(filter_buttons), 0, "No filter buttons found on the page.")

        # Click the first available filter
        first_filter = filter_buttons[0]
        filter_label = first_filter.text.strip()
        first_filter.click()

        # Wait for the list to update
        self.wait.until(
            EC.staleness_of(filter_buttons[0])
        )
        updated_cards = wait_for_events_to_load(self.wait)

        # The list should still have cards
        self.assertGreater(
            len(updated_cards), 0,
            f"After clicking filter '{filter_label}', no events are displayed."
        )

    # -------------------------------------------------------------------------
    # TC-03: Clicking an event opens its detail page
    # -------------------------------------------------------------------------
    def test_click_event_opens_detail_page(self):
        """TC-03: Clicking an event card navigates to the event detail page."""
        self.driver.get(EVENTS_URL)

        event_cards = wait_for_events_to_load(self.wait)
        self.assertGreater(len(event_cards), 0, "No event cards found to click.")

        # Record the URL before clicking
        url_before = self.driver.current_url

        # Click the first event card title or the card itself
        first_card = event_cards[0]
        try:
            title_link = first_card.find_element(By.CSS_SELECTOR, "a, h2, h3, .event-title")
            title_link.click()
        except Exception:
            first_card.click()

        # Wait for navigation to a different page
        self.wait.until(EC.url_changes(url_before))

        url_after = self.driver.current_url
        self.assertNotEqual(url_before, url_after, "URL did not change after clicking an event card.")
        self.assertIn("event", url_after.lower(), "New URL does not look like an event detail page.")

    # -------------------------------------------------------------------------
    # TC-04 (Negative): Search with no matching query shows empty state
    # -------------------------------------------------------------------------
    def test_search_with_no_results_shows_empty_state(self):
        """TC-04 (Negative): A nonsense search query returns no events and shows a message."""
        self.driver.get(EVENTS_URL)
        wait_for_events_to_load(self.wait)

        # Find the search input
        search_input = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[type='search'], input[placeholder*='earch'], .search-input input")
            )
        )

        # Type a query that should not match anything
        search_input.clear()
        search_input.send_keys("xyzxyzxyz999")
        search_input.submit()

        # Wait a moment for results to update
        import time
        time.sleep(2)  # acceptable here — no reliable trigger to wait on after submit

        # Either no cards are present, or an empty-state element is shown
        cards = self.driver.find_elements(
            By.CSS_SELECTOR, "app-event-card, .event-card, .events-item"
        )
        empty_state = self.driver.find_elements(
            By.CSS_SELECTOR, ".no-events, .empty-state, .not-found, [class*='no-result']"
        )

        self.assertTrue(
            len(cards) == 0 or len(empty_state) > 0,
            "Expected no results or an empty-state message, but event cards are still displayed."
        )

    # -------------------------------------------------------------------------
    # TC-05 (Negative): Page title is correct (smoke check)
    # -------------------------------------------------------------------------
    def test_page_title_is_not_empty(self):
        """TC-05 (Negative/Smoke): The page has a non-empty title (basic load check)."""
        self.driver.get(EVENTS_URL)

        # Wait for the Angular app to initialize
        self.wait.until(lambda d: d.title != "")

        title = self.driver.title
        self.assertTrue(len(title) > 0, "Page title is empty — the page may have failed to load.")
        self.assertNotIn("404", title, "Page title contains '404' — page not found.")
        self.assertNotIn("Error", title, "Page title contains 'Error'.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
