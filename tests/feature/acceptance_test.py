#For run this test case type to command line "py.test -v -s pytest_2/test_class.py --browser firefox" in project directory
#For run this test case with html report type to command line "py.test -v -s test_class.py --browser firefox --html=report.html"
#py.test -v -s pytest_2/test_class.py --browser firefox --alluredir report
#allure generate report
import pytest

from pages.page_for_practice import *


# @pytest.mark.usefixtures("oneTimeSetUp", "setUp") #fixtures applied for each test method in class
@allure.feature("Acceptance tests")

class TestClassAcceptance():

    # # common fixtures for each test in class
    # @pytest.fixture(autouse=True)               #argument "autouse=True" has the same meaning as @pytest.mark.usefixtures("Some_Fixtures")
    # def setUpInClass(self, oneTimeSetUp):
    #     #get value from fixture oneTimeSetUp
    #     self.value_from_fixture = self.value

    @allure.story("Login by user")
    def test_login(self):
        typeValue()
        clickButton()
        # assert 10 == self.value_from_fixture

    @allure.story("Check profile")
    def test_profile(self):
        clickButton()
        check_profile()


    @allure.story("Check Out")
    def test_check_out(self):
        typeValue()
        clickButton()
        check_out()
