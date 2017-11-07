from common.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class PracticePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickForumButoon(self):
        elem = self.waitForElement(By.XPATH, "//a[contains(.,'Форум')]")
        elem.click()

    def click_on_Angular(self):
        elem = self.waitForAngularJS(By.XPATH, "//img[@class='oppia-logo oppia-logo-wide']")
        elem.click()

    def click_on_Angular2(self):
        self.waitForAngular2(By.XPATH,"//input[@id='login']").send_keys("test-user")
        self.waitForAngular2(By.XPATH, "//input[@id='password']").send_keys("testtest")
        elem = self.waitForAngular2(By.XPATH, "//button[@id='sign-in']")
        elem.click()
        assert  self.waitForAngular2(By.XPATH, "//div[contains(text(),'100011110000')]") is not None

def typeValue():
    with allure.step("type value"):
         assert 10 == 10


def clickButton():
    with allure.step("Click Button"):
         assert 10 == 10


def check_profile():
    with allure.step("chech profile data"):
         assert 10 == 8


def check_out():
    with allure.step("Pay something"):
         assert 10 == 10