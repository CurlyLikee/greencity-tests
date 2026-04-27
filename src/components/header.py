"""
header.py — Header component for GreenCity.
Contains: sign-in, language switcher, navigation links.
"""
import allure
from selenium.webdriver.common.by import By

from src.components.base_component import BaseComponent


class Header(BaseComponent):
    """Header bar component — sign-in, language, navigation."""

    # Locators (relative to header root)
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".header_sign-in-link")
    LANGUAGE_SWITCHER = (By.XPATH, ".//ul[@aria-label='language switcher']")
    LANGUAGE_EN = (By.XPATH, ".//span[contains(text(), 'En')]")
    LANGUAGE_UA = (By.XPATH, ".//span[contains(text(), 'Uk')]")
    EVENTS_LINK = (
        By.XPATH,
        ".//a[contains(@class, 'url-name') and (contains(., 'Події') or contains(., 'Events'))]",
    )
    ECO_NEWS_LINK = (
        By.XPATH,
        ".//a[contains(@class, 'url-name') and (contains(., 'Еко новини') or contains(., 'Eco news'))]",
    )

    @allure.step("Click Sign In button")
    def click_sign_in(self):
        self.find_element(*self.SIGN_IN_BUTTON).click()

    @allure.step("Switch language to '{language}'")
    def switch_language(self, language: str):
        """Switch UI language. Accepts 'en' or 'ua'."""
        self.find_element(*self.LANGUAGE_SWITCHER).click()
        if language.lower() == "en":
            self.find_element(*self.LANGUAGE_EN).click()
        elif language.lower() == "ua":
            self.find_element(*self.LANGUAGE_UA).click()
        else:
            raise ValueError(f"Unsupported language: {language}")

    @allure.step("Get Events navigation link")
    def get_events_link(self):
        return self.find_element(*self.EVENTS_LINK)

    @allure.step("Navigate to Events page")
    def navigate_to_events(self):
        self.find_element(*self.EVENTS_LINK).click()

    @allure.step("Navigate to Eco News page")
    def navigate_to_eco_news(self):
        self.find_element(*self.ECO_NEWS_LINK).click()
