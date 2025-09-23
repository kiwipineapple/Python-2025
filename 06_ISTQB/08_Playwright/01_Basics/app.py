# cmd > pip install playwright
# cmd > playwright install        (to install the browsers for the playwright)

import os
from pathlib import Path
from playwright.sync_api import sync_playwright

os.chdir(Path(__file__).parent)

with sync_playwright() as p:
    # Open the browser
    # browser = p.chromium.launch(headless = True) # Browser will be in background (invisible)
    # browser = p.chromium.launch(headless = False) # Browser will be appeared and visible
    browser = p.firefox.launch(headless=False)

    # Create a new page
    page = browser.new_page()

    # Open the website
    page.goto("https://en.wikipedia.org/wiki/List_of_HTTP_status_codes")

    # Get the page title
    print(f"Page title: {page.title()}")

    # Take a screenshot
    page.screenshot(path="./assert/01_example.png")

    # close the browser
    browser.close()
