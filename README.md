# GreenCity — Events Page Test Cases

## Project Description

This repository contains manual test cases and automated UI tests for the **Events** page of the GreenCity web application.

Automated tests are written in **Python** using **Selenium WebDriver** and the built-in **unittest** framework.

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
    ├── test_events_page.py
    └── utils.py
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
python -m unittest discover tests
```

### 3. Run a specific test

```bash
python -m unittest tests.test_events_page.EventsPageTests.test_events_list_is_displayed_on_page_load
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
