"""
base_page.py — Base Page Object for GreenCity.
Contains common elements shared across all pages: header, language switcher, navigation.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base page with common header elements (sign-in, language, navigation)."""

    # Locators
    SIGN_IN_BUTTON = (
        By.CSS_SELECTOR,
        ".header_navigation-menu-right-list > .header_sign-in-link",
    )
    LANGUAGE_SWITCHER = (By.XPATH, "//ul[@aria-label='language switcher']")
    LANGUAGE_EN_OPTION = (By.XPATH, ".//span[contains(text(), 'En')]")
    LANGUAGE_UA_OPTION = (By.XPATH, ".//span[contains(text(), 'Uk')]")

    ECO_NEWS_LINK = (
        By.XPATH,
        "//header//a[contains(@class, 'url-name') and (contains(., 'Еко новини') or contains(., 'Eco news'))]",
    )
    EVENTS_LINK = (
        By.XPATH,
        "//header//a[contains(@class, 'url-name') and (contains(., 'Події') or contains(., 'Events'))]",
    )

    # Constructor
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Helper: explicit wait wrappers
    def _find(self, locator):
        """Find element with explicit wait (presence)."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def _find_all(self, locator):
        """Find all matching elements with explicit wait."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def _click(self, locator):
        """Wait for element to be clickable, then click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    # Sign-in
    def get_sign_in_button(self):
        return self._find(self.SIGN_IN_BUTTON)

    def click_sign_in(self):
        self._click(self.SIGN_IN_BUTTON)

    # Language switcher
    def switch_language(self, language: str):
        """Switch the UI language. Accepts 'en' or 'ua'."""
        self._click(self.LANGUAGE_SWITCHER)
        if language.lower() == "en":
            self._click(self.LANGUAGE_EN_OPTION)
        elif language.lower() == "ua":
            self._click(self.LANGUAGE_UA_OPTION)
        else:
            raise ValueError(f"Unsupported language: {language}")

    # Navigation
    def get_events_link(self):
        return self._find(self.EVENTS_LINK)

    def navigate_to_events(self):
        self._click(self.EVENTS_LINK)

    def get_eco_news_link(self):
        return self._find(self.ECO_NEWS_LINK)

    def navigate_to_eco_news(self):
        self._click(self.ECO_NEWS_LINK)

    # Page title
    def get_page_title(self) -> str:
        """Return the browser page title."""
        return self.driver.title

    def get_current_url(self) -> str:
        """Return the current URL."""
        return self.driver.current_url
