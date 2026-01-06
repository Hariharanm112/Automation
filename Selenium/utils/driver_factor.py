import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class BaseDriver:
    def __init__(self):
        self.driver = None
    def setup(self):
        """
        Setup the WebDriver, initialize the browser with specific options.
        """
        options = Options()
        options.add_argument("--start-maximized")  # Start with maximized window
        options.add_argument("--disable-notifications")  # Disable notifications (optional)
        options.add_argument("--headless=new")  # Use "--headless=new" for modern Chrome versions
        options.add_argument("--no-sandbox")  # Required for Linux CI
        options.add_argument("--disable-dev-shm-usage")  # Avoid memory issues in containers
        options.add_argument("--disable-gpu")
        # Initialize the ChromeDriver using WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Set implicit wait time (seconds)
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
