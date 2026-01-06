import pytest
from utils.driver_factor import BaseDriver

@pytest.fixture(scope="function")
def driver():
    base_driver = BaseDriver()
    base_driver.setup()
    driver = base_driver.driver
    yield driver
    base_driver.teardown()
