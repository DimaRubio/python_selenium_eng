import allure
import pytest
import unittest

class BaseTest():

    def pass_subunit(self, URL, count_lessons, answers, type_quiz = "radio"):
        with allure.step("pass lessons"):
            self.pm.lesson_content.go_to(URL)
            self.pm.lesson_content.pass_lesson(count_lessons)
        with allure.step("pass quiz"):
            #this block executed when quiz is a set of radio buttons
            if type_quiz is "radio":
                self.pm.quiz_content.choose_an_answer(answers[0])
            #this block executed when quiz is a set of input fields
            else:
                self.pm.quiz_content.type_an_answer(answers[0])
            with allure.step("check results"):
                assert answers[1] is int(self.pm.quiz_content.get_count_right_questions())
                # self.pm.quiz_content.click_on_next_button()

    @allure.story("User has ability to pass unit")
    def pass_unit_1_1(self, answers_1 = ((2, 4, 1, 3, 4), 5)):      #description: answers_1 = ((tuple of answers), count right answers in tuple))
        with allure.step("pass subunit 1.1"):
            self.pass_subunit("/course/introduction-to-efl/455-the-efl-industry-overview/", 4, answers_1)

    @allure.story("User has ability to pass unit")
    def pass_unit_1_2(self, answers_1 = ((2, 3, 3, 1, 4), 5), answers_2 = ((1, 2, 2, 2, 1), 5),
                      answers_3 = ((6, 3, 5, 1, 2), 5), answers_4 = ((2, 1, 4, 4, 3, 2, 4, 3), 8)):
        with allure.step("pass subunit 1.2.1"):
            self.pass_subunit("/course/introduction-to-efl/3026-reasons-for-learning-2/", 2, answers_1)
        with allure.step("pass subunit 1.2.2"):
            self.pass_subunit("/course/introduction-to-efl/3029-learner-differences-2/", 1, answers_2)
        with allure.step("pass subunit 1.2.3"):
            self.pass_subunit("/course/introduction-to-efl/3031-learning-characteristics-2/", 1, answers_3, "input")
        with allure.step("pass subunit 1.2.4"):
            self.pass_subunit("/course/introduction-to-efl/3033-student-motivation-2/", 2, answers_4)

    @allure.story("User has ability to pass unit")
    def pass_unit_1_3(self, answers_1 = ((4, 1, 2, 2, 3, 3), 6), answers_2 = ((8, 2, 4, 3, 1, 5), 6)):
        with allure.step("pass subunit 1.3.1"):
            self.pass_subunit("/course/introduction-to-efl/3846-types-of-institutions-for-efl-careers/", 1, answers_1)
        with allure.step("pass subunit 1.3.2"):
            self.pass_subunit("/course/introduction-to-efl/3847-types-of-contracts-and-general-expectations/", 1,  answers_2, "input")