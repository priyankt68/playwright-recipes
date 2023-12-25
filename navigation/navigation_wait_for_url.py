from playwright.sync_api import sync_playwright
from time import perf_counter, sleep


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, 
        slow_mo=500
    )
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://ecommerce-playground.lambdatest.io/")

    # Click a link that leads to a new page
    page.get_by_role("button", name="My account").click()

    # wait until the URL of the page contains '/login
    page.wait_for_url('**/login')

    # perform actions on the page.
    page.get_by_placeholder("E-Mail Address").click()
    page.get_by_placeholder("E-Mail Address").fill("user1@lambdatest.io")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("unitest123")

    # perform actions on the page.

    browser.close()
    
    