import os

import time

from common.base_test import BaseTest
import pytest
from pages.page_manager import PageManager
import allure
from ddt import ddt, data, unpack
from utilities.recognize_csv import recognizeCSVData


@pytest.mark.usefixtures("create_user")
@allure.feature("Pass exams")
class TestPassExams(BaseTest):

    @allure.story("checking reported answers with saved ones")
    def test_checking_reported_answers_with_saved_answers(self):
        with allure.step("pass subunit 1.1"):
            self.check_reported_answers_with_saved("/course/introduction-to-efl/455-the-efl-industry-overview/", 4, ((1, 1, 1, 1, 1), None))
        with allure.step("pass subunit 1.2.1"):
            self.check_reported_answers_with_saved("/course/introduction-to-efl/3026-reasons-for-learning-2/", 2, ((1, 1, 1, 1, 1), None))
        with allure.step("pass subunit 1.2.2"):
            self.check_reported_answers_with_saved("/course/introduction-to-efl/3029-learner-differences-2/", 1, ((1, 1, 1, 1, 1), None))
        with allure.step("pass subunit 1.2.3"):
            self.check_reported_answers_with_saved("/course/introduction-to-efl/3031-learning-characteristics-2/", 1, ((1, 2, 3, 4, 5), None), "input")
        with allure.step("pass subunit 1.2.4"):
            self.check_reported_answers_with_saved("/course/introduction-to-efl/3033-student-motivation-2/", 2, ((1, 1, 1, 1, 1, 1, 1, 1), None))
        with allure.step("pass subunit 1.3.1"):
            self.check_reported_answers_with_saved("/course/introduction-to-efl/3846-types-of-institutions-for-efl-careers/", 1, ((1, 1, 1, 1, 1, 1), None))
        with allure.step("pass subunit 1.3.2"):
            self.check_reported_answers_with_saved("/course/introduction-to-efl/3847-types-of-contracts-and-general-expectations/", 1, ((1, 2, 3, 4, 5, 6), None), "input")