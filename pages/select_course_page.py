from common.base_page import BasePage
from selenium.webdriver.common.by import By


class OnlineCoursePage(BasePage):

    def __init__(self):
        super().__init__()

    _professional_button = "//a[@href='/professional-course/']"
    _enroll_button = "//a[contains(.,'ENROLL NOW')]"

    def click_on_professional_course_button(self):
        self.click_on_element_by_xpath(self._professional_button)

    def click_on_enroll_button(self):
        self.click_on_element_by_xpath(self._enroll_button)
