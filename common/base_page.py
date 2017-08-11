import allure
from selenium.webdriver.common.by import By
from common.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


class BasePage(SeleniumDriver):

    # Locators
    _base_url = "https://dev.mytefl.com"
    _msg_error ="//ul[@class='woocommerce-error']"
    _msg_congratulations = "//h3[contains(.,'Congratulations!!')]"
    _admin_bar = "//div[@id='wpadminbar']"
    _dashboard_button = "//div[contains(@class,'l2')]//*[@class='nav_bar_login_menu']/li"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()


    def delete_cookie(self):
        self.driver.delete_all_cookies()
        # self.goTo("")   #refresh page is must have

    def go_to(self, value):
        with allure.step("go to: {}".format(value)):
            if "http" not in value:
                self.driver.get(self._base_url + value)
            else:
                self.driver.get(value)


    def get_msg_error(self):
        return self.wait_for_element(By.XPATH, self._msg_error)

    def get_msg_congratulations(self):
        return self.wait_for_element(By.XPATH, self._msg_congratulations)

    def get_admin_bar(self):
        return self.wait_for_element(By.XPATH, self._admin_bar)

    def get_dashboard_button(self):
        return self.wait_for_element(By.XPATH, self._dashboard_button)

    def title_contains_text(self, titleToVerify):
        try:
            actual_title = self.get_title()
            return self.util.verifyTextContains(actual_title, titleToVerify)
        except:
            print_stack()
            return False

    def element_present(self, element):
        if element is not None:
            return True
        else:
            return False

    def scroll_page(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_on_element_by_xpath(self, locator):
        self.wait_for_element(By.XPATH, locator)
        self.driver.execute_script("element = document.evaluate(\"" + locator + "\", document, null, XPathResult.ANY_TYPE, null).iterateNext();if (element !== null) {element.click();};")

    def click_on_element_by_js(self, element):
        self.driver.execute_script("element = arguments[0]; if (element !== null) {element.click();};", element)

    def send_keys_by_xpath(self, locator, value):
        self.wait_for_element(By.XPATH, locator)
        self.driver.execute_script("element = document.evaluate(\"" + locator + "\", document, null, XPathResult.ANY_TYPE, null).iterateNext();if (element !== null) {element.value=\"" + value + "\";};")

    def click_on_element_use_action(self, by_type, locator):
        element = self.wait_for_element(by_type, locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        action.click(element).perform()