import pytest
from pages.login_page import AmazonLoginPage
from pages.product_search_shoe import ProductSearch
from utils.config import Config

@pytest.mark.parametrize("product", ["shoe", "hat", "bat", "watch"])
def test_search_products(driver, product):
    # login first
    login_page = AmazonLoginPage(driver)
    login_page.login(Config.AMAZON_USERNAME, Config.AMAZON_PASSWORD)

    # search product
    search_page = ProductSearch(driver, product)
    search_page.search_bar()
    first_product_text = search_page.comparison()

    # assert
    assert product.lower() in first_product_text.lower(), f"Expected '{product}' in '{first_product_text}'"
