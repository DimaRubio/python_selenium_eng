import os

import time

from common.base_test import BaseTest
import pytest
from pages.page_manager import PageManager
import allure
from ddt import ddt, data, unpack
from utilities.recognize_csv import recognizeCSVData

@pytest.mark.usefixtures("create_user")
@allure.feature("Pass units")
class TestPassUnit(BaseTest):

    @allure.story("User hasn't ability learn next unit if your current unit scope less than 65%")
    @pytest.mark.run(before='test_reset_unit_one')
    def test_inaccessibility_next_unit_over_click_on_next_button(self):

        with allure.step("Puss first unit"):
            self.pass_unit_1_1(answers_1= ((2, 2, 2, 2, 2), 1))
            self.pass_unit_1_2()
            self.pass_unit_1_3(answers_1 = ((2,2,2,2,2,2), 2))

        with allure.step("Try to learn first lesson in second unit"):
            self.pm.quiz_content.click_on_next_button()
            self.pm.lp_courses.driver.switch_to.alert.accept()

    @allure.story("User hasn't ability learn next unit if your current unit scope less than 65%")
    @pytest.mark.run(after='test_inaccessibility_next_unit_over_click_on_next_button')
    def test_inaccessibility_next_unit_over_select_lesson(self):
        self.pm.lp_courses.go_to("/lp-courses/")
        with allure.step("Try to learn first lesson in second unit"):
            #click on first lesson in unit №2
            self.pm.lp_courses.click_on_ref_item("3406")

        with allure.step("Check that alert with warning is displayed"):
            assert "less than 65" in self.pm.lp_courses.driver.switch_to.alert.text
            self.pm.lp_courses.driver.switch_to.alert.accept()

    @allure.story("Calculate course scope")
    @pytest.mark.run(after='test_inaccessibility_next_unit_over_select_lesson')
    def test_calculate_course_scope(self):
        self.pm.lp_courses.go_to("/lp-profile/Dmytroqa/quizzes/")
        with allure.step("Calculate course scope"):
            scope = self.pm.lp_courses.calculate_course_scope()
            fdf = int(scope)
        with allure.step("Check result"):
            assert int(scope) >= 0

    @allure.story("User has ability reset unit scope")
    def test_reset_unit_one(self):
        with allure.step("Get current unit scope"):
            self.pm.lp_courses.go_to("/lp-profile/Dmytroqa/quizzes/")
            prev_scope = self.pm.lp_courses.get_unit_score(1)
        self.pm.lp_courses.go_to("/lp-courses/")
        with allure.step("Reset Unit"):
            self.pm.lp_courses.click_on_reset_button()
            with allure.step("confirming action 1"):
                self.pm.lp_courses.wait_for_allert()
                self.pm.lp_courses.driver.switch_to.alert.accept()
                # self.pm.lp_courses.wait_for_allert_is_not_present()
            with allure.step("confirming action 2"):
                # self.pm.lp_courses.wait_for_allert()
                time.sleep(0.5)
                self.pm.lp_courses.wait_for_allert()
                self.pm.lp_courses.driver.switch_to.alert.accept()
        with allure.step("Get current unit scope after reset"):
            self.pm.lp_courses.driver.back()
            self.pm.lp_courses.driver.refresh()
            current_scope = self.pm.lp_courses.get_unit_score(1)
        with allure.step("Make sure that reset was successful"):
            assert prev_scope > current_scope

    @allure.story("User has ability learn next unit if your current unit scope more than 65%")
    @pytest.mark.run(after='test_reset_unit_one')
    def test_accessibility_next_unit(self):
        with allure.step("Puss first unit"):
            self.pass_unit_1_1()
            self.pass_unit_1_2()
            self.pass_unit_1_3()
        with allure.step("Try to learn first lesson in second unit"):
            self.pm.lp_courses.go_to("/lp-courses/")
            with allure.step("click on first lesson in unit №2"):
                self.pm.lp_courses.click_on_ref_item("3406")
        with allure.step("Check that lesson materials page is displayed"):
            assert "3406-first-impressions" in self.pm.lp_courses.driver.current_url

    @allure.story("User hasn't ability reset the same unit twice")
    @pytest.mark.run(after='test_accessibility_next_unit')
    def test_reset_unit_twice(self):
        self.pm.lp_courses.go_to("/lp-courses/")
        with allure.step("Check that reset button is not displayed"):
            assert self.pm.lp_courses.reset_button_is_displayed() is False
