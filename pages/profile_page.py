import allure

from common.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ProfilePage(BasePage):

    def __init__(self):
        super().__init__()
#1
    _first_name_field = "//input[@id='billing_first_name']"
    _last_name_field = "//input[@id='billing_last_name']"
    _phone_field = "//input[@id='billing_phone']"
    _email_field = "//input[@id='billing_email']"
    _country_field = "billing_country"
    _address_field = "//input[@id='billing_address_1']"
    _town_field = "//input[@id='billing_city']"
    _state_field = "//input[@id='billing_state']"
    _postcode_field = "//input[@id='billing_postcode']"
    _submit_button = "//div[@class='edit-account']/input"

    def get_first_name_field(self):
        return self.wait_for_element(By.XPATH, self._first_name_field)

    def get_last_name_field(self):
        return self.wait_for_element(By.XPATH, self._last_name_field)

    def get_phone_field(self):
        return self.wait_for_element(By.XPATH, self._phone_field)

    def get_email_field(self):
        return self.wait_for_element(By.XPATH, self._email_field)

    def get_adress_field(self):
        return self.wait_for_element(By.XPATH, self._address_field)

    def get_town_field(self):
        return self.wait_for_element(By.XPATH, self._town_field)

    def get_state_field(self):
        return self.wait_for_element(By.XPATH, self._state_field)

    def get_postcode_field(self):
        return self.wait_for_element(By.XPATH, self._postcode_field)

    def get_country_field(self):
        self.driver.execute_script(
            "document.getElementById(\"" + self._country_field + "\").style.display = \"inline\";")
        return Select(self.driver.find_element(By.ID, self._country_field))

    def fill_personal_information_form(self, first_name, last_name, phone, country ="China", address ="address", town = "town", state = "state", postcode = "10001"):
        with allure.step("enter first name"):
            self.get_first_name_field().clear()
            self.get_first_name_field().send_keys(first_name)
        with allure.step("enter last name"):
            self.get_last_name_field().clear()
            self.get_last_name_field().send_keys(last_name)
        with allure.step("enter phone"):
            self.get_phone_field().clear()
            self.get_phone_field().send_keys(phone)
        with allure.step("select country"):
            self.get_country_field().select_by_value(country)
        with allure.step("enter address"):
            self.get_adress_field().clear()
            self.get_adress_field().send_keys(address)
        with allure.step("enter town"):
            self.get_town_field().clear()
            self.get_town_field().send_keys(town)
        with allure.step("enter state"):
            self.get_state_field().clear()
            self.get_state_field().send_keys(state)
        with allure.step("enter postcode"):
            self.get_postcode_field().clear()
            self.get_postcode_field().send_keys(postcode)

    def click_on_submit_button(self):
        self.click_on_element_by_xpath(self._submit_button)