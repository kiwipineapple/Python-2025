import os
from pathlib import Path
from playwright.sync_api import sync_playwright
import pytest


os.chdir(Path(__file__).parent)

CITY = "Berlin"
EXPECTED = "Berlin, DE"


# mit 2 browser testen
@pytest.mark.parametrize("browser_name", ["chromium", "firefox"])
def test_openweathermap_search(browser_name):
    with sync_playwright() as p:

        # Test with Several Browsers
        browser = getattr(p, browser_name).launch(headless=False)

        # Create a Context Manager for creating the page later
        context = browser.new_context()

        # Create a new page
        page = context.new_page()

        # Open the website
        page.goto("https://openweathermap.org/")

        # Select (CLick) the Text Box in the Search Box
        page.locator(".search-container input[type='text']").click()

        # Fill the City Name
        page.fill(".search-container input[type='text']", CITY)

        page.keyboard.press("Enter")

        #  Wait for the Search DropDown Menu List Items [Li]
        page.wait_for_selector(".search-dropdown-menu li")

        # Get the results from the drop down
        results = page.locator(".search-dropdown-menu li")

        # Get the first Item from the Drop Down Menu
        first_result = results.nth(0).inner_text()

        assert EXPECTED in first_result, f"Expected '{EXPECTED}' in search result, got '{first_result}'"

        # Take a screenshot
        page.screenshot(path="./assert/05_example.png")

        # close the browser
        browser.close()
