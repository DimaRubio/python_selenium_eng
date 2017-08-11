from common.base_page import BasePage
from selenium.webdriver.common.by import By

class QuizContentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _next_button = "//div[contains(@class,'course-item-next')]/a"
    _prev_button = "//div[contains(@class,'course-item-prev')]/a"
    _next_question_button = "//button[@data-nav='next']"
    _prev_question_button = "//button[@data-nav='prev']"
    _submit_exam_button = "//button[@data-area='nav']"
    _count_question = "//span[@class='quiz-mark']/small"
    _count_right_questions = "//span[@class='quiz-mark']" #block with mark, to use 'text' to get the result
    _answer_number = "//ul[@class='learn-press-question-options']/li"
    _answer_number_str = "//div[@id='learn-press-quiz-description']//li"
    _question_number_str = ".quiz-question-content"


    def get_next_button(self):
        return  self.wait_for_element(By.XPATH, self._next_button)

    def get_id_next_button(self):
        return self.get_next_button().get_attribute("data-id")

    def get_prev_button(self):
        return  self.wait_for_element(By.XPATH, self._prev_button)

    def get_next_question_button(self):
        return self.wait_for_element(By.XPATH, self._next_question_button)

    def click_on_next_question_button(self):
        self.click_on_element_by_js(self.get_next_question_button())

    def get_prev_question_button(self):
        return self.wait_for_element(By.XPATH, self._prev_question_button)

    def click_on_prev_question_button(self):
        self.click_on_element_by_js(self.get_prev_question_button())

    def choose_an_answer(self, answer_list):
        count = len(answer_list)
        for answer_number in answer_list:
            locator = self._answer_number + "[{}]//input".format(answer_number)
            self.click_on_element_by_js(self.wait_for_element(By.XPATH, locator))
            #to take up the next question
            if count > 1 :
                self.click_on_next_question_button()
            #Submit exam
            else:
                self.click_on_element_by_xpath(self._submit_exam_button)
            count -= 1

    def type_an_answer(self, answer_list):
        count = len(answer_list)

        for answer_number in answer_list:
            locator = self._answer_number_str + "[{}]".format(answer_number)
            # wait while question transferred over ajax
            self.wait_for_element(By.CSS_SELECTOR, self._question_number_str)
            self.click_on_element_by_js(self.wait_for_element(By.XPATH, locator))
            #to take up the next question
            if count > 1 :
                self.click_on_next_question_button()
            #Submit exam
            else:
                self.click_on_element_by_xpath(self._submit_exam_button)
            count -= 1

    def get_count_right_questions(self):
        mark_arr = self.wait_for_element(By.XPATH, self._count_right_questions).text.split(' ')
        mark = mark_arr[0]
        return mark

    def click_on_next_button(self):
        self.click_on_element_by_js(self.get_next_button())