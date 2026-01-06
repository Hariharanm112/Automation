# pages/product_search.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductSearch:
    def __init__(self, driver, product_name):
        self.driver = driver
        self.product_name = product_name
        self.SEARCH = (By.ID, "twotabsearchtextbox")
        self.SUBMIT = (By.ID, "nav-search-submit-button")
        self.FIRST_PRODUCT = (By.XPATH,f"(//span[contains(text(),'{product_name}')])[1]")

    def search_bar(self):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH)
        )
        search_input.clear()
        search_input.send_keys(self.product_name)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT)
        ).click()

    def comparison(self):
        # Wait up to 20 seconds for the element to be present in DOM
        first_product = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.FIRST_PRODUCT)
        )
        # Then wait until it’s visible
        first_product_visible = WebDriverWait(self.driver, 10).until(
            EC.visibility_of(first_product)
        )
        return first_product_visible.text

