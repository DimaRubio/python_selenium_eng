import allure
from selenium.webdriver.support.select import Select
from common.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckOutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _term_checkbox = "//input[@id='terms']"
    _order_button = "//input[@id='place_order']"
    _payment_form = "//li[contains(@class,'braintree')]"
    _cc_number_field ="//input[@id='braintree-card-number']"
    _cc_month_dropdown = "//select[@id='braintree-card-expiry-month']"
    _cc_year_dropdown = "//select[@id='braintree-card-expiry-year']"
    _cc_cvc_field = "//input[@id='braintree-card-cvc']"


    def click_on_term_checkBox(self):
        self.click_on_element_by_xpath(self._term_checkbox)

    def click_on_order_button(self):
        self.click_on_element_by_xpath(self._order_button)

    def getPaymentForm(self):
        return self.waitForElement(By.XPATH, self._payment_form)

    def get_cc_number_field(self):
        return self.waitForElement(By.XPATH, self._cc_number_field)

    def get_cc_month_dropdown(self):
        element = self.waitForElement(By.XPATH, self._cc_month_dropdown)
        return Select(element)

    def get_cc_year_dropdown(self):
        element = self.waitForElement(By.XPATH, self._cc_year_dropdown)
        return Select(element)

    def get_cc_cvc_field(self):
        return self.waitForElement(By.XPATH, self._cc_cvc_field)

    def fill_form(self, cc_number, cc_exp_month, cc_exp_year, cvc):
        with allure.step("enter card number"):
            self.send_keys_by_xpath(self._cc_number_field, cc_number)
        with allure.step("set expiry date|month"):
            self.get_cc_month_dropdown().select_by_value(cc_exp_month)
        with allure.step("set expiry date|year"):
            self.get_cc_year_dropdown().select_by_value(cc_exp_year)
        with allure.step("enter cvc code"):
            self.get_cc_cvc_field().send_keys(cvc)

    def check_out_purchase_result(self, expected_result):
        if expected_result == "0":
            try:
                assert self.get_msg_error() is not None
                return False
            except:
                return True
        else:
            try:
               assert self.get_msg_congratulations() is not None
               return True
            except:
               return False


