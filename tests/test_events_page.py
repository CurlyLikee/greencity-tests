"""
test_events_page.py — Automated UI tests for the GreenCity Events page.
Uses: pytest + Allure + Page Object Model + Components.
"""
import allure
import pytest


@allure.feature("Events Page")
class TestEventsPage:
    """Tests for https://www.greencity.cx.ua/#/greenCity/events"""

    # TC-01: Events list is displayed on page load
    @allure.story("Display events list")
    @allure.title("TC-01: Events list is visible after opening the Events page")
    def test_events_list_is_displayed_on_page_load(self, events_page):
        """TC-01: Events list is visible after opening the Events page."""
        with allure.step("Wait for event cards to load"):
            cards = events_page.get_event_card_elements()

        with allure.step("Verify at least one event card is present"):
            assert len(cards) > 0, \
                "Expected at least one event card on the page, but found none."

    # TC-02: Filter by category updates the displayed events
    @allure.story("Filter events by category")
    @allure.title("TC-02: Clicking a category filter changes the displayed events")
    def test_filter_by_category_updates_list(self, events_page):
        """TC-02: Clicking a category filter changes the displayed events."""
        with allure.step("Wait for initial page load"):
            old_cards = events_page.get_event_card_elements()

        with allure.step("Get filter panel and click first filter"):
            panel = events_page.get_filter_panel()
            assert panel.get_count() > 0, "No filter buttons found on the page."
            filter_label = panel.click_filter(0)

        with allure.step("Wait for cards to reload after filter"):
            updated_cards = events_page.wait_for_cards_reload(old_cards)

        with allure.step(f"Verify events are displayed after filter '{filter_label}'"):
            assert len(updated_cards) > 0, \
                f"After clicking filter '{filter_label}', no events are displayed."

    # TC-03: Clicking an event opens its detail page
    @allure.story("Open event details")
    @allure.title("TC-03: Clicking an event card navigates to the event detail page")
    def test_click_event_opens_detail_page(self, events_page):
        """TC-03: Clicking an event card navigates to the event detail page."""
        with allure.step("Get event cards"):
            cards = events_page.get_cards()
            assert len(cards) > 0, "No event cards found to click."

        with allure.step("Record URL before click"):
            url_before = events_page.get_current_url()

        with allure.step("Click the first event card title"):
            cards[0].click_title()

        with allure.step("Wait for URL to change"):
            events_page.wait.until(
                lambda d: d.current_url != url_before
            )

        with allure.step("Verify navigation to event detail page"):
            url_after = events_page.get_current_url()
            assert url_before != url_after, \
                "URL did not change after clicking an event card."
            assert "event" in url_after.lower(), \
                "New URL does not look like an event detail page."

    # TC-04 (Negative): Search with no matching query shows empty state
    @allure.story("Search with no results")
    @allure.title("TC-04: A nonsense search query returns no events")
    def test_search_with_no_results_shows_empty_state(self, events_page):
        """TC-04 (Negative): A nonsense search query returns no events."""
        with allure.step("Wait for page to load fully"):
            events_page.get_event_card_elements()

        with allure.step("Enter nonsense search query"):
            events_page.search("xyzxyzxyz999")

        with allure.step("Wait for search results to update"):
            events_page.wait_for_search_results()

        with allure.step("Verify no results or empty-state message"):
            visible_cards = events_page.get_visible_card_count()
            no_results = events_page.has_no_results()
            assert visible_cards == 0 or no_results, \
                "Expected no results or an empty-state message, but cards are still displayed."

    # TC-05 (Negative): Page title is correct (smoke check)
    @allure.story("Page title smoke check")
    @allure.title("TC-05: The page has a non-empty, valid title")
    def test_page_title_is_not_empty(self, events_page):
        """TC-05 (Negative/Smoke): The page has a non-empty title."""
        with allure.step("Wait for page title to appear"):
            title = events_page.wait_for_title()

        with allure.step("Verify title is not empty"):
            assert len(title) > 0, \
                "Page title is empty — the page may have failed to load."

        with allure.step("Verify title does not contain error indicators"):
            assert "404" not in title, "Page title contains '404' — page not found."
            assert "Error" not in title, "Page title contains 'Error'."
