import allure

from common.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class OnlineCoursePage(BasePage):

    def __init__(self):
        super().__init__()
#1
    _professional_button = "//a[@href='/professional-course/']"

    def click_on_professional_course_button(self):
        self.click_on_element_by_xpath(self._professional_button)
#2
    _enroll_button = "//a[contains(.,'ENROLL NOW')]"
    _first_name_field = "//input[@name='billing_first_name']"
    _last_name_field = "//input[@name='billing_last_name']"
    _email_field = "//input[@name='billing_email']"
    _phone_field = "//input[@name='billing_phone']"
    _country_field = "//select[@name='billing_country']"
    _submit_button = "//a[@id='add_to_cart_form']"

    def click_on_enroll_button(self):
        self.click_on_element_by_xpath(self._enroll_button)

    def fill_personal_information_form(self, first_name, last_name, email, phone, country ="CR"):
        with allure.step("enter first name"):
            self.wait_for_element(By.XPATH, self._first_name_field).send_keys(first_name)
        with allure.step("enter last name"):
            self.wait_for_element(By.XPATH, self._last_name_field).send_keys(last_name)
        with allure.step("enter email"):
            self.wait_for_element(By.XPATH, self._email_field).send_keys(email)
        with allure.step("enter phone"):
            self.wait_for_element(By.XPATH, self._phone_field).send_keys(phone)
        with allure.step("select country"):
            # self.driver.execute_script("document.getElementById(\""+self._country_field +"\").style.display = \"inline\";")
            Select(self.driver.find_element(By.XPATH, self._country_field)).select_by_value(country)

    def click_on_submit_button(self):
        self.click_on_element_by_xpath(self._submit_button)

