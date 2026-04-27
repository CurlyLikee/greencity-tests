"""
conftest.py — Pytest fixtures for GreenCity UI tests.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.pages.events_page import EventsPage


@pytest.fixture
def driver():
    """Create and yield a Chrome WebDriver instance, then quit."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    chrome = webdriver.Chrome(options=options)
    chrome.implicitly_wait(5)
    yield chrome
    chrome.quit()


@pytest.fixture
def events_page(driver):
    """Open the Events page and return its Page Object."""
    page = EventsPage(driver)
    page.open()
    return page
