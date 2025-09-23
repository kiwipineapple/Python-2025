import os
from pathlib import Path
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

os.chdir(Path(__file__).parent)

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

try:

    with sync_playwright() as p:

        browser = p.firefox.launch(headless=False)

        page = browser.new_page()

        page.goto("https://home.openweathermap.org/users/sign_in")

        page.wait_for_selector("input[type='email']")

        page.fill("input[type='email']", email)
        page.fill("input[type='password']", password)

        # CLick on Submit Button
        page.click("input[value='Submit']")

        # Wait for the navigation to be completed
        page.wait_for_timeout(3000)  # wait 3 seconds

        success_message = page.query_selector("text=Signed in successfully")

        if success_message:
            print("Login successfully!")

            # Get the page title
            print(f"Page title: {page.title()}")

            # Take a screenshot
            page.screenshot(path="./assert/02_example.png")

        else:
            print("Login failed")
except TimeoutError:
    print("Page elemens took too long time to be loaded")

except Exception:
    print("Some Error occured")

finally:
    # close the browser
    browser.close()
