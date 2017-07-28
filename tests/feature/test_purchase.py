from common.base_test import BaseTest
import pytest
from pages.page_manager import PageManager
import allure
from ddt import ddt, data, unpack
from utilities.recognize_csv import recognizeCSVData

@pytest.mark.usefixtures("user_admin","classSetup")
@allure.feature("Purchase feature")
@ddt
class TestPurchaseClass(BaseTest):

    @pytest.fixture(scope="class")
    def classSetup(self, request, driver_set_up):
        driver = driver_set_up.instance
        pageManager = PageManager(driver)
        if request.cls is not None:
            request.cls.pageManager = pageManager
        with allure.step("log in on site"):
            pageManager.login.logInOnSite(self.login, self.password)
        yield
        with allure.step("log Out"):
            pageManager.login.logOut()

    # @data(*recognizeCSVData(os.getcwd()+"/resourses/testdata.csv"))
    @allure.story("To purchase course")
    @data(*recognizeCSVData("/home/dmytro.bolyachin/TestDir/Python/myTEFL/resourses/testdata.csv"))
    @unpack
    def test_purchase_course(self,  expected_result, cc_number, cc_exp_month, cc_exp_year, cc_cvv):
        pm = self.pageManager
        pm.login.goTo('https://dev.mytefl.com/online-onsite-courses/online-tefl-courses/')
        with allure.step("select professional course"):
            pm.online_course.click_on_professional_course_button()
        with allure.step("click on enroll course button"):
            pm.online_course.click_on_enroll_button()
        with allure.step("scroll page to card payment form"):
            pm.check_out.scrollToElement(pm.check_out.getPaymentForm())
        with allure.step("click on a checkbox"):
            pm.check_out.click_on_term_checkBox()
        with allure.step("fill card payment form"):
            pm.check_out.fill_form(cc_number, cc_exp_month, cc_exp_year, cc_cvv)
        with allure.step("course purchase"):
            pm.check_out.click_on_order_button()
        with allure.step("chek out a result"):
            self.assertEqual(int(expected_result),pm.check_out.check_out_purchase_result(expected_result))


