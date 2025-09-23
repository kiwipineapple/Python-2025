import os
from pathlib import Path
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

os.chdir(Path(__file__).parent)

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

with sync_playwright() as p:
    # Open the browser
    # browser = p.chromium.launch(headless = True) # Browser will be in background (invisible)
    # browser = p.chromium.launch(headless = False) # Browser will be appeared and visible
    browser = p.firefox.launch(headless=False)

    # Create a new page
    page = browser.new_page()

    # Open the website
    page.goto("https://home.openweathermap.org/users/sign_in")

    page.wait_for_selector("input[type='email']")

    page.fill("input[type='email']", email)
    page.fill("input[type='password']", password)

    # CLick on Submit Button
    page.click("input[value='Submit']")

    # Wait for the navigation to be completed

    # Way 1:
    success_message = page.query_selector("text=Signed in successfully")

    if success_message:
        print("Login successfully!")

        # Get the page title
        print(f"Page title: {page.title()}")

        # Take a screenshot
        page.screenshot(path="./assert/02_example.png")

    else:
        print("Login failed")

    # Way 2:
    success_message = page.query_selector(
        ".panel-body:has-text('Signed in successfully.')")

    if success_message:
        print("Login successfully 2.!")

        # Get the page title
        print(f"Page title: {page.title()}")

        # Take a screenshot
        page.screenshot(path="./assert/03_example.png")

    else:
        print("Login failed")

    # close the browser
    browser.close()
