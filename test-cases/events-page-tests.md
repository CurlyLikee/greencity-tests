# Test Cases — Events Page (GreenCity)

**Page under test:** https://www.greencity.cx.ua/#/greenCity/events

---

## TC-01: Display list of events on page load

**Title:** Events list is displayed when the user opens the Events page

**Preconditions:**
- The user is not logged in
- The browser has a stable internet connection
- URL: `https://www.greencity.cx.ua/#/greenCity/events`

**Test Steps:**

| Step | Action | Data | Expected Result |
|------|--------|------|-----------------|
| 1 | Open the browser | - | Browser is open |
| 2 | Enter the URL in the address bar | `https://www.greencity.cx.ua/#/greenCity/events` | Page starts loading |
| 3 | Wait for the page to fully load | - | Page is loaded, no error messages are shown |
| 4 | Look at the main content area | - | A list of events is displayed with titles, dates, and images |
| 5 | Scroll down the page | - | More events are visible; layout remains consistent |

---

## TC-02: Filter events by category

**Title:** Filtering events by category shows only relevant results

**Preconditions:**
- The user is on the Events page (`https://www.greencity.cx.ua/#/greenCity/events`)
- At least one filter/category option is visible on the page
- Events are loaded and displayed

**Test Steps:**

| Step | Action | Data | Expected Result |
|------|--------|------|-----------------|
| 1 | Locate the filter/category section on the page | - | Filter options are visible (e.g. tags or category buttons) |
| 2 | Click on one of the available category filters | e.g. "ECO_NEWS" or any visible tag | The selected category is highlighted/active |
| 3 | Wait for the list to update | - | The page reloads the event list |
| 4 | Check the displayed events | - | Only events matching the selected category are shown |
| 5 | Click the same filter again to deselect it (or click "All") | - | All events are displayed again |

---

## TC-03: Open event details page

**Title:** Clicking on an event opens its detailed view

**Preconditions:**
- The user is on the Events page
- At least one event card is visible

**Test Steps:**

| Step | Action | Data | Expected Result |
|------|--------|------|-----------------|
| 1 | Locate any event card in the list | - | Event card is visible with a title and image |
| 2 | Click on the event card title or image | - | The browser navigates to the event detail page |
| 3 | Check the URL | - | URL changes to reflect the specific event (e.g. `.../events/123`) |
| 4 | Check the page content | - | Full event description, date, location, and author are displayed |
| 5 | Click the browser's Back button | - | User is returned to the Events list page |

---

## TC-04 (Negative): Search with a query that returns no results

**Title:** Searching for a non-existent event shows an appropriate "no results" message

**Preconditions:**
- The user is on the Events page
- A search input field is available on the page

**Test Steps:**

| Step | Action | Data | Expected Result |
|------|--------|------|-----------------|
| 1 | Locate the search input field | - | Search field is visible and clickable |
| 2 | Click on the search field | - | The field becomes active (cursor appears) |
| 3 | Type a search query that is unlikely to match any event | `xyzxyzxyz123` | Text appears in the search field |
| 4 | Press **Enter** or click the search button | - | Search is submitted |
| 5 | Check the results area | - | No event cards are displayed; a message like "No results found" or similar is shown |
| 6 | Clear the search field | - | The full events list is restored |

---

## TC-05 (Negative): Open Events page with no internet connection

**Title:** Events page shows an error or fallback message when the network is unavailable

**Preconditions:**
- The browser is open
- The user **disconnects from the internet** before navigating

**Test Steps:**

| Step | Action | Data | Expected Result |
|------|--------|------|-----------------|
| 1 | Disconnect from the internet (turn off Wi-Fi or use browser DevTools -> Network -> Offline) | - | Network is unavailable |
| 2 | Navigate to the Events page | `https://www.greencity.cx.ua/#/greenCity/events` | Page attempts to load |
| 3 | Wait a few seconds | - | Page does not crash the browser |
| 4 | Check the page content | - | An error message, loading spinner with timeout, or offline notice is displayed instead of the event list |
| 5 | Reconnect to the internet and refresh | - | Events list loads correctly |
