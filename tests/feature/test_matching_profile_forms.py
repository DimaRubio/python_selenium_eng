import os

import time

from common.base_test import BaseTest
import pytest
from pages.page_manager import PageManager
import allure
from ddt import ddt, data, unpack
from utilities.recognize_csv import recognizeCSVData

@pytest.mark.usefixtures("classSetup")
@allure.feature("Verifying values in forms")
class TestMatchingProfileForms(BaseTest):

    @pytest.fixture(scope="class")
    def classSetup(self, request, page_manager_set_up):
        pm = page_manager_set_up
        if request.cls is not None:
            request.cls.pm = pm
        yield
        with allure.step("log Out"):
            pm.login.delete_cookie()

    @allure.story("Verifying values in checkout form after entered ones in subscription form")
    @pytest.mark.parametrize("test_input",[("firstName","lastName","test@ttttest.qa","+3000123456"),
                                           ("","","","")])
    def test_matching_subscription_form_with_checkout_forms(self, test_input):
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