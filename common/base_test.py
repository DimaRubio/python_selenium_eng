import pytest
import unittest

class BaseTest(unittest.TestCase):
    pass

    # @pytest.fixture(scope="class", autouse=True)
    # def manage_driver(self, request, driver_set_up):
    #     pass
    #     # driver_set_up.start()
    #     # request.addfinalizer(driver_set_up.stop)
    #     # yield
    #     # driver_set_up.stop()