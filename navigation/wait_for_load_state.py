from playwright.sync_api import sync_playwright

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

    page.wait_for_load_state() # the promise resolves after "load" event.  
    # It allows you to wait for various load states, such as 'load', 'domcontentloaded', and 'networkidle'
    # 'domcontentloaded': Waits for the HTML to be parsed and the DOM to be constructed.
    # 'networkidle': Waits until there are no network connections for a certain period, indicating that the page has finished its network activity.
    
    """ Why
    We wait for the page to load completely before interacting with it. This ensures that validatiions occurs before the page is fully loaded.
    Dynamic content may not load in time, some AJAX request might take some more time and hence waiting makes sense.
    By waiting for the load state, we ensure the DOM is constructure and external resources like images, stylesheets, and fonts are loaded before interacting with the page.
    """    
    # perform actions on the page.
    page.get_by_placeholder("E-Mail Address").click()
    page.get_by_placeholder("E-Mail Address").fill("priyankt68@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("LambdaTest123")
    page.get_by_role("button", name="Login").click()
    
    browser.close()
    