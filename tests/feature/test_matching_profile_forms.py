import os

import time

from common.base_test import BaseTest
import pytest
from pages.page_manager import PageManager
import allure
from ddt import ddt, data, unpack
from utilities.recognize_csv import recognizeCSVData

@pytest.mark.usefixtures("classSetup")
@allure.feature("Verifying user data")
class TestMatchingProfileForms(BaseTest):

    @pytest.fixture(scope="class")
    def classSetup(self, request, page_manager_set_up):
        pm = page_manager_set_up
        if request.cls is not None:
            request.cls.pm = pm
        yield
        with allure.step("log Out"):
            pm.login.delete_cookie()

    @allure.story("Verifying values in checkout after entered ones in subscription form")
    @pytest.mark.parametrize("test_input",[("firstName","lastName","test@ttttest.qa","+3000123456"),
                                           ("","","","")])
    def test_verifying_values_in_checkout_after_entered_ones_in_subscription_form(self, test_input):
        first_name = test_input[0]
        last_name = test_input[1]
        email = test_input[2]
        phone = test_input[3]

        self.pm.select_course.go_to("/online-onsite-courses/online-tefl-courses/advanced-course/")
        with allure.step("Filling subscription form"):
            self.pm.select_course.fill_personal_information_form(first_name, last_name, email, phone)
            self.pm.select_course.click_on_submit_button()
        with allure.step("Verifying saved values in checkout form with entered values"):
            assert first_name == self.pm.check_out.get_first_name_field().get_attribute('value')
            assert last_name == self.pm.check_out.get_last_name_field().get_attribute('value')
            assert phone == self.pm.check_out.get_phone_field().get_attribute('value')
            assert email == self.pm.check_out.get_email_field().get_attribute('value')

    @allure.story("check user data after saving ones in profile")
    @pytest.mark.run(after='test_verifying_values_in_checkout_after_entered_ones_in_subscription_form')
    @pytest.mark.parametrize("input_value",
                             [("firstName","lastName","+3000123456", "China", "address1", "town1", "state1", "12121"),
                             ("","","","China", "","","","")])
    def test_check_saved_values_in_profile(self, input_value):
        with allure.step("log in on site"):
            self.pm.login.logIn_on_site("test20170803164724@test.qa", 123456)
        self.pm.select_course.go_to("/lp-profile")
        with allure.step("Filling profile form"):
            self.pm.profile.fill_personal_information_form(input_value[0], input_value[1], input_value[2], input_value[3], input_value[4], input_value[5], input_value[6], input_value[7])
            self.pm.profile.click_on_submit_button()
        with allure.step("Verifying saved values in checkout form with entered values in profile"):
            with allure.step("check first name"):
                assert input_value[0] == self.pm.profile.get_first_name_field().get_attribute('value')
            with allure.step("check last name"):
                assert input_value[1] == self.pm.profile.get_last_name_field().get_attribute('value')
            with allure.step("check phone"):
                assert input_value[2] == self.pm.profile.get_phone_field().get_attribute('value')
            with allure.step("check country"):
                assert input_value[3] == self.pm.profile.get_country_field().first_selected_option.text
            with allure.step("check address"):
                assert input_value[4] == self.pm.profile.get_adress_field().get_attribute('value')
            with allure.step("check city"):
                assert input_value[5] == self.pm.profile.get_town_field().get_attribute('value')
            with allure.step("check state"):
                assert input_value[6] == self.pm.profile.get_state_field().get_attribute('value')
            with allure.step("check postcode"):
                assert input_value[7] == self.pm.profile.get_postcode_field().get_attribute('value')

    @allure.story("Verifying values in checkout after entered ones in profile")
    @pytest.mark.run(after='test_check_saved_values_in_profile')
    @pytest.mark.parametrize("input_value",
                             [("firstName","lastName","+3000123456", "China", "address1", "town1", "state1", "12121"),
                             ("","","","China", "","","","")])
    def test_verifying_values_in_checkout_after_entered_ones_in_profile(self, input_value):
        self.pm.select_course.go_to("/lp-profile")
        with allure.step("Filling profile form"):
            self.pm.profile.fill_personal_information_form(input_value[0], input_value[1], input_value[2], input_value[3], input_value[4], input_value[5], input_value[6], input_value[7])
            self.pm.profile.click_on_submit_button()
        with allure.step("Verifying saved values in checkout form with entered values in profile"):
            self.pm.select_course.go_to("/checkout/")
            with allure.step("check first name"):
                assert input_value[0] == self.pm.check_out.get_first_name_field().get_attribute('value')
            with allure.step("check last name"):
                assert input_value[1] == self.pm.check_out.get_last_name_field().get_attribute('value')
            with allure.step("check phone"):
                assert input_value[2] == self.pm.check_out.get_phone_field().get_attribute('value')
            with allure.step("check country"):
                assert input_value[3] == self.pm.check_out.get_country_field().first_selected_option.text
            with allure.step("check address"):
                assert input_value[4] == self.pm.check_out.get_adress_field().get_attribute('value')
            with allure.step("check city"):
                assert input_value[5] == self.pm.check_out.get_town_field().get_attribute('value')
            with allure.step("check state"):
                assert input_value[6] == self.pm.check_out.get_state_field().get_attribute('value')
            with allure.step("check postcode"):
                assert input_value[7] == self.pm.check_out.get_postcode_field().get_attribute('value')


