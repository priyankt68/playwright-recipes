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

    # perform actions on the page.
    print("Loading login form.")

    login_form = page.get_by_placeholder("E-Mail Address")
    login_form.wait_for()

    # perform actions on the page.
    login_form.click()
    login_form.fill("user1@lambdatest.io")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("unitest123")

    browser.close()
    
    