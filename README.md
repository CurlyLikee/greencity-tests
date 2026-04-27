# GreenCity — Events Page Test Cases

## Project Description

This repository contains manual test cases and automated UI tests for the **Events** page of the GreenCity web application.

Automated tests are written in **Python** using **Selenium WebDriver** and the built-in **unittest** framework.  
Tests follow the **Page Object Pattern (PO)** for clean separation of locators, page actions, and test logic.

---

## Page Under Test

**URL:** https://www.greencity.cx.ua/#/greenCity/events

---

## Repository Structure

```
greencity-tests/
├── README.md
├── requirements.txt
├── test-cases/
│   └── events-page-tests.md
└── tests/
    ├── utils.py                            # Driver factory
    ├── test_events_page.py                 # Test cases (TC-01 … TC-05)
    └── pages/
        ├── __init__.py
        ├── base_page.py                    # BasePage — header, language, navigation
        ├── events_page.py                  # EventsPage — events list, filters, search
        └── components/
            ├── __init__.py
            ├── base_component.py           # BaseComponent — scoped element search
            └── event_card_component.py     # EventCardComponent — single event card
```

---

## Page Object Hierarchy

```
BasePage                         (header, sign-in, language, navigation)
  └── EventsPage                 (event cards, filters, search, items count)

BaseComponent                    (scoped find_element within a root WebElement)
  └── EventCardComponent         (event name, click title, click 'More')
```

---

## How to Run the Tests

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

> You also need **Google Chrome** installed and a matching **ChromeDriver** available in your PATH.

### 2. Run all tests

```bash
cd tests
python -m unittest discover .
```

### 3. Run a specific test

```bash
cd tests
python -m unittest test_events_page.EventsPageTests.test_events_list_is_displayed_on_page_load
```

---

## Test Cases Overview

| ID | Test name | Type |
|----|-----------|------|
| TC-01 | `test_events_list_is_displayed_on_page_load` | Positive |
| TC-02 | `test_filter_by_category_updates_list` | Positive |
| TC-03 | `test_click_event_opens_detail_page` | Positive |
| TC-04 | `test_search_with_no_results_shows_empty_state` | Negative |
| TC-05 | `test_page_title_is_not_empty` | Negative / Smoke |

---

## Author

**[Alona Hruieva]**  
QA Practice Assignment - GreenCity Events Page Automation
