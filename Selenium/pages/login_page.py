from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.config import Config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Config.AMAZON_URL  # Use URL from config

        # Locators
        self.sign_in = (By.ID, "nav-link-accountList")
        self.email = (By.ID, "ap_email_login")
        self.submit = (By.ID, "continue")
        self.password = (By.ID, "ap_password")
        self.sign_in_button = (By.ID, "signInSubmit")

    def open(self):
        # Open the Amazon Login page
        self.driver.get(self.url)

    def login(self, username, password):
        self.open()  # Open the Amazon Login page
        # Enter username/email
        self.driver.find_element(*self.sign_in).click()
        # Wait for email field to be visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email)
        ).send_keys(username)
        self.driver.find_element(*self.submit).click()  # Click continue button

        # Wait for password field to be visible (improve this with explicit waits)
        self.driver.find_element(*self.password).send_keys(password)

        # Click sign-in button
        self.driver.find_element(*self.sign_in_button).click()
