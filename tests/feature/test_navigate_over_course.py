import os

from common.base_test import BaseTest
import pytest
from pages.page_manager import PageManager
import allure
from ddt import ddt, data, unpack
from utilities.recognize_csv import recognizeCSVData


@pytest.mark.usefixtures("create_user")
@allure.feature("Navigate over course")
@ddt
class TestNavigateOverCourse:

    @allure.story("User has ability to mark lesson as completed")
    @pytest.mark.run(order=1)
    def test_completed_lesson(self):
        self.pm.lesson_content.go_to("/course/introduction-to-efl/455-the-efl-industry-overview/")
        el = self.pm.lesson_content.get_continue_button()
        if "SAVE AND CONTINUE" in el.text:
            self.pm.lesson_content.click_on_element_by_js(el)
            self.pm.lesson_content.click_on_element_by_js(self.pm.lesson_content.get_prev_button())
            assert "SAVED" in self.pm.lesson_content.get_continue_button_disable().text
        else:
            assert False

    #Depending on test_completed_lesson, because lesson№1 must be completed for first data pair

    @allure.story("User has ability go to the next lesson, if it has been completed")
    @pytest.mark.run(after='test_completed_lesson')
    @pytest.mark.parametrize("url_input, expected", [
        ("/course/introduction-to-efl/455-the-efl-industry-overview/", 1),
        ("/course/introduction-to-efl/457-popular-efl-destinations/", 0)
        ])
    def test_go_to_next_lesson(self, url_input, expected):
        # self.pm = PageManager(driver)
        self.pm.lesson_content.go_to(url_input)
        prev_id = self.pm.lesson_content.get_id_next_button()
        self.pm.lesson_content.click_on_element_by_js(self.pm.lesson_content.get_next_button())
        current_id = self.pm.lesson_content.get_id_next_button()
        assert (prev_id < current_id) == bool(expected)

    @allure.story("User has ability go to the previously completed lesson")
    @pytest.mark.run(after='test_completed_lesson')
    def test_go_to_prev_lesson(self):
        self.pm.lesson_content.go_to("/course/introduction-to-efl/457-popular-efl-destinations/")
        prev_id = self.pm.lesson_content.get_id_next_button()
        self.pm.lesson_content.click_on_element_by_js(self.pm.lesson_content.get_prev_button())
        current_id = self.pm.lesson_content.get_id_next_button()
        assert (prev_id > current_id) == True

    @allure.story("User has't ability to skip quiz")
    @pytest.mark.run(before='test_go_to_next_lesson')
    def test_skip_quiz(self):
        with allure.step("pass first lessons"):
            self.pm.lesson_content.go_to("/course/introduction-to-efl/455-the-efl-industry-overview/")
            self.pm.lesson_content.pass_lesson(4)
        with allure.step("wait until quiz loading"):
            self.pm.quiz_content.get_next_question_button()
        with allure.step("Check that skip quiz is not possible"):
            prev_id = self.pm.quiz_content.get_id_next_button()
            self.pm.quiz_content.click_on_next_button()
            current_id = self.pm.quiz_content.get_id_next_button()
            assert (prev_id == current_id) == True