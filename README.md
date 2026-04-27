# GreenCity — Events Page UI Automation

## Project Description

Automated UI tests for the **Events** page of the GreenCity web application.

**Stack:** Python · Selenium WebDriver · Pytest · Allure Report  
**Architecture:** Page Object Model (POM) + Component-based approach

---

## Page Under Test

**URL:** https://www.greencity.cx.ua/#/greenCity/events

---

## Repository Structure

```
greencity-tests/
├── conftest.py                # Pytest fixtures (driver setup/teardown)
├── pytest.ini                 # Pytest + Allure config
├── requirements.txt
├── .gitignore
├── src/
│   ├── pages/
│   │   ├── base_page.py       # BasePage — driver, waits, helpers
│   │   └── events_page.py     # EventsPage — events listing logic
│   └── components/
│       ├── base_component.py  # BaseComponent — scoped element search
│       ├── header.py          # Header — sign-in, language, navigation
│       ├── filter_panel.py    # FilterPanel — tag/category filters
│       └── event_card.py      # EventCard — single event card
├── tests/
│   └── test_events_page.py    # 5 automated test cases
└── test-cases/
    └── events-page-tests.md   # Manual test case descriptions
```

---

## Architecture

```
BasePage                        (driver, WebDriverWait, helpers)
  └── EventsPage                (events listing, search, components)

BaseComponent                   (scoped find_element within root WebElement)
  ├── Header                    (sign-in, language, navigation)
  ├── FilterPanel               (tag/category filter buttons)
  └── EventCard                 (event name, click title, click 'More')
```

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

> You also need **Google Chrome** and a matching **ChromeDriver** in your PATH.

### 2. Run tests

```bash
pytest --alluredir=allure-results
```

### 3. Generate Allure report

```bash
allure serve allure-results
```

---

## Test Cases

| ID    | Test name                                      | Type            |
|-------|------------------------------------------------|-----------------|
| TC-01 | `test_events_list_is_displayed_on_page_load`   | Positive        |
| TC-02 | `test_filter_by_category_updates_list`          | Positive        |
| TC-03 | `test_click_event_opens_detail_page`            | Positive        |
| TC-04 | `test_search_with_no_results_shows_empty_state` | Negative        |
| TC-05 | `test_page_title_is_not_empty`                  | Negative / Smoke|

---

## Author

**Alona Hruieva**  
QA Practice — GreenCity Events Page Automation
