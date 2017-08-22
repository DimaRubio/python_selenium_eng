import datetime

import allure
from selenium.webdriver.support.select import Select
from common.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckOutPage(BasePage):

    def __init__(self):
        super().__init__()

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

    def get_payment_form(self):
        return self.wait_for_element(By.XPATH, self._payment_form)

    def get_cc_number_field(self):
        return self.wait_for_element(By.XPATH, self._cc_number_field)

    def get_cc_month_dropdown(self):
        element = self.wait_for_element(By.XPATH, self._cc_month_dropdown)
        return Select(element)

    def get_cc_year_dropdown(self):
        element = self.wait_for_element(By.XPATH, self._cc_year_dropdown)
        return Select(element)

    def get_cc_cvc_field(self):
        return self.wait_for_element(By.XPATH, self._cc_cvc_field)

    def fill_card_form(self, cc_number, cc_exp_month, cc_exp_year, cvc):
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

    _first_name_field = "//input[@id='billing_first_name']"
    _last_name_field = "//input[@id='billing_last_name']"
    _phone_field = "//input[@id='billing_phone']"
    _email_field = "//input[@id='billing_email']"
    _ver_email_field = "//input[contains(@id,'billing_em_ver')]"
    _country_field = "billing_country"
    _address_field = "//input[@id='billing_address_1']"
    _town_field = "//input[@id='billing_city']"
    _state_field = "//input[@id='billing_state']"
    _postcode_field = "//input[@id='billing_postcode']"

    def create_new_user(self):
        with allure.step("filling user data form"):
            time = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
            user_name = "User" + time
            last_name = "Last" + user_name
            email = "test{0}@test.qa".format(time)
            self.fill_personal_information_form(user_name, last_name, time, email)
            self.fill_card_form("4111111111111111","10","2018","123")
            self.click_on_term_checkBox()
        with allure.step("submit form"):
            self.click_on_order_button()
        with allure.step("check that enroll was successful"):
            assert self.get_dashboard_button() is not None

    def fill_personal_information_form(self, first_name, last_name, phone, email, country ="CR", address ="address", town = "town", state = "state", postcode = "10001"):
        ver_email_field = email
        with allure.step("enter first name"):
            self.wait_for_element(By.XPATH, self._first_name_field).send_keys(first_name)
        with allure.step("enter last name"):
            self.wait_for_element(By.XPATH, self._last_name_field).send_keys(last_name)
        with allure.step("enter phone"):
            self.wait_for_element(By.XPATH, self._phone_field).send_keys(phone)
        with allure.step("enter email"):
            self.wait_for_element(By.XPATH, self._email_field).send_keys(email)
        with allure.step("enter verification email"):
            self.wait_for_element(By.XPATH, self._ver_email_field).send_keys(ver_email_field)
        with allure.step("select country"):
            self.driver.execute_script("document.getElementById(\""+self._country_field +"\").style.display = \"inline\";")
            Select(self.driver.find_element(By.ID, self._country_field)).select_by_value(country)
        with allure.step("enter address"):
            self.wait_for_element(By.XPATH, self._address_field).send_keys(address)
        with allure.step("enter town"):
            self.wait_for_element(By.XPATH, self._town_field).send_keys(town)
        with allure.step("enter state"):
            self.wait_for_element(By.XPATH, self._state_field).send_keys(state)
        with allure.step("enter state"):
            self.wait_for_element(By.XPATH, self._postcode_field).send_keys(postcode)

