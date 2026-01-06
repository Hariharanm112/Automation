import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class BaseDriver:
    def __init__(self):
        self.driver = None

    from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class BaseTest:
    def setup(self):
        """
        Setup the Chrome WebDriver with options suitable for CI (headless, no notifications).
        """
        options = Options()
        # Browser window options
        options.add_argument("--start-maximized")        # Optional for local runs
        options.add_argument("--disable-notifications")  # Disable browser notifications

        # Headless mode for Jenkins/Linux servers
        options.add_argument("--headless=new")  # Use "--headless=new" for modern Chrome versions
        options.add_argument("--no-sandbox")    # Required for Linux CI
        options.add_argument("--disable-dev-shm-usage")  # Avoid memory issues in containers
        options.add_argument("--disable-gpu")   # Optional, sometimes needed for CI

        # Initialize WebDriver using WebDriver Manager
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        # Implicit wait (seconds)
        self.driver.implicitly_wait(10)

    def teardown(self):
        """
        Teardown the WebDriver, close the browser and quit the session.
        """
        time.sleep(2)  # Optional: Sleep to see the results before quitting
        self.driver.quit()

    def get_driver(self):
        """
        Return the WebDriver instance to allow interaction with the browser.
        """
        return self.driver
