from common.base_page import BasePage
from selenium.webdriver.common.by import By

class LessonContentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _next_button = "//div[contains(@class,'course-item-next')]/a"
    _prev_button = "//div[contains(@class,'course-item-prev')]/a"
    _continue_button_enable = "//div[contains(@class,'save-continue')]//button"
    _continue_button_disable = "//div[contains(@class,'save-continue')]//button[@disabled='disabled']"

    def get_next_button(self):
        return  self.wait_for_element(By.XPATH, self._next_button)

    def get_prev_button(self):
        return  self.wait_for_element(By.XPATH, self._prev_button)

    def get_continue_button(self):
        self.wait_for_element(By.XPATH, self._next_button)
        return self.wait_for_element(By.XPATH, self._continue_button_enable, 3)

    def get_continue_button_disable(self):
        self.wait_for_element(By.XPATH, self._next_button)
        return self.driver.find_element(By.XPATH, self._continue_button_disable)

    def get_id_next_button(self):
        return self.get_next_button().get_attribute("data-id")

    def pass_lesson(self,value):
        count = value
        while count > 0:
            #Get save-continue button
            el = self.get_continue_button()
            if el is not None:
                #Click on save-continue button
                self.click_on_element_by_js(el)
            #Click on Next button
            else:
                self.click_on_element_by_js(self.get_next_button())
            count -= 1


