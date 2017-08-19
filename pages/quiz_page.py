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
    _mark = "//span[@class='quiz-mark']" #block with mark, to use 'text' to get the result
    _answer_number = "//ul[@class='learn-press-question-options']/li"
    _answer_number_input = "//div[@id='learn-press-quiz-description']//li"
    _question_number_input = ".quiz-question-content"
    _saved_answer = "//input[@checked='checked']/.."
    _saved_answer_input = "//div[@class='question-passage']//input"


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

    def get_reported_answers(self, answer_list):
        count = len(answer_list)
        values = []
        for answer_number in answer_list:
            locator = self._answer_number + "[{}]//input".format(answer_number)
            el = self.wait_for_element(By.XPATH, locator)
            self.click_on_element_by_js(el)
            values.append(self.wait_for_element(By.XPATH, self._answer_number+"[{}]/label".format(answer_number)).text)
            #to take up the next question
            if count > 1 :
                self.click_on_next_question_button()
            #Submit exam
            else:
                self.click_on_element_by_xpath(self._submit_exam_button)
            count -= 1
        return values

    #for quiz is a set of radio buttons
    def get_saved_answer_list(self, count_lessons):
        self.wait_for_element(By.XPATH, self._mark)
        list = self.driver.find_elements(By.XPATH, self._saved_answer)
        values = []
        for item in list:
            values.append(item.text)
        return values

    # for quiz is a set of input fields
    def get_saved_answer_list_from_inputs(self, count_lessons):
        self.wait_for_element(By.XPATH, self._mark)
        list = self.driver.find_elements(By.XPATH, self._saved_answer_input)
        values = []
        for item in list:
            values.append(item.get_attribute('value'))
        return values

    def type_an_answer(self, answer_list):
        count = len(answer_list)

        for answer_number in answer_list:
            locator = self._answer_number_input + "[{}]".format(answer_number)
            # wait while question transferred over ajax
            self.wait_for_element(By.CSS_SELECTOR, self._question_number_input)
            self.click_on_element_by_js(self.wait_for_element(By.XPATH, locator))
            #to take up the next question
            if count > 1 :
                self.click_on_next_question_button()
            #Submit exam
            else:
                self.click_on_element_by_xpath(self._submit_exam_button)
            count -= 1

    def get_reported_answers_from_inputs(self, answer_list):
        count = len(answer_list)
        values = []
        for answer_number in answer_list:
            locator = self._answer_number_input + "[{}]".format(answer_number)
            # wait while question transferred over ajax
            self.wait_for_element(By.CSS_SELECTOR, self._question_number_input)
            el = self.wait_for_element(By.XPATH, locator)
            self.click_on_element_by_js(el)
            values.append(el.text)
            #to take up the next question
            if count > 1 :
                self.click_on_next_question_button()
            #Submit exam
            else:
                self.click_on_element_by_xpath(self._submit_exam_button)
            count -= 1
        return values


    def get_mark(self):
        mark_arr = self.wait_for_element(By.XPATH, self._mark).text.split(' ')
        mark = mark_arr[0]
        return mark

    def click_on_next_button(self):
        self.click_on_element_by_js(self.get_next_button())