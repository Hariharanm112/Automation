from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductSearchHat:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.SEARCH = (By.ID, "twotabsearchtextbox")  # Amazon search input
        self.SUBMIT = (By.ID, "nav-search-submit-button")  # Search button
        self.COMPARE=(By.XPATH,"(//span[contains(text(), 'shoe')])[1]")

    def search_bar_hat(self, productname):
        # Wait until the search box is clickable
        search_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH)
        )

        # Click the search input to focus
        search_input.click()

        # Type the product name
        search_input.send_keys(productname)

        # Wait for search button and click
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT)
        ).click()

    def comparison_hat(self):
        """Return text of first product containing 'shoe'"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.COMPARE)
        ).text

