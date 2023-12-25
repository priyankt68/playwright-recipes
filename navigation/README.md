## Wait for a Custom Element - wait_for()
The wait_for() method in Playwright is used to ensure that a specific custom element is fully loaded and ready for interaction before proceeding with further actions. For example, you can locate an element using a selector (in this case, by placeholder) and then use wait_for() to make sure that the element is present and ready for use:

```
login_form = page.get_by_placeholder("E-Mail Address")
login_form.wait_for()
```

## Wait for a URL to Load in Mainframe - wait_for_url()
The wait_for_url() method is employed to pause script execution until the URL of the page matches a specified pattern. This is useful when navigating to a new page and waiting for it to fully load before performing subsequent actions:
```
# Click a link that leads to a new page
page.get_by_role("button", name="My account").click()

# Wait until the URL of the page contains '/login'
page.wait_for_url('**/login')

```

## Wait of 4 Types While Loading a Page - wait_until
The wait_until option in the page.goto() method allows you to specify the criteria for considering the page as "loaded." Playwright supports four types of waiting strategies:

1. 'commit': Waits until the response is received.
2. 'domcontentloaded': Waits until the HTML is parsed, and <script> is executed.
3. 'load': Default behavior, waits until the HTML is loaded along with all resources.
4. 'networkidle': Waits until network operations stop (useful for dynamic pages with asynchronous content loading).

```

    page.goto(
        "https://ecommerce-playground.lambdatest.io/",
        # Response received
        # wait_until='commit',

        # HTML parsed and <script> executed
        # wait_until='domcontentloaded',

        # Default, HTML loaded along with resources
        # wait_until='load',

        # Network operations stopped
        wait_until='networkidle',
    )

```