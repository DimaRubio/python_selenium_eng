import datetime

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from common.selenium_driver import *
from selenium.common.exceptions import *
from traceback import print_stack
from utilities.util import Util
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    # Locators
    _base_url = "https://dev.mytefl.com"
    _msg_error ="//ul[@class='woocommerce-error']"
    _msg_congratulations = "//h3[contains(.,'Congratulations!!')]"
    _admin_bar = "//div[@id='wpadminbar']"
    _dashboard_button = "//div[contains(@class,'l2')]//*[@class='nav_bar_login_menu']/li"

    def __init__(self, browser = None):
        self.driver_obj = SelenDriver(browser)
        self.driver = self.driver_obj.driver

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

    def wait_for_element(self, by_type, locator, timeout = 20) -> WebElement:
        element = None
        try:
            print("Waiting for maximum :: {0} :: seconds for element :: {1} :: to be clickable {2}".format(str(timeout), locator, str(datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"))))
            wait = WebDriverWait(self.driver, timeout)
            #Wait for Javascript to load
            wait.until(lambda driver: self.driver.execute_script("return document.readyState") == "complete")
            # Uncomment line below if web-app using jQuery
            wait.until(lambda driver: self.driver.execute_script("return jQuery.active == 0"))
            print("JS request is completed at time: " + str(datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")))
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            print("Element appeared on the web page {0}".format(locator))
        except TimeoutException as e:
            print(str(e))
            # raise TimeoutException
        if element is not None:
            return element

    def wait_for_angularJS(self, by_type, locator, timeout = 20):
        element = None
        try:
            print("Waiting for maximum :: {0} :: seconds for element :: {1} :: to be clickable {2}".format(str(timeout), locator, str(datetime.datetime.now().strftime("%Y%m%d %H%M%S"))))
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda driver: self.driver.execute_script("return document.readyState") == "complete")
            wait.until(lambda driver: self.driver.execute_script("return (window.angular !== undefined) && (angular.element(document).injector() !== undefined) && (angular.element(document).injector().get('$http').pendingRequests.length === 0)"))
            print("JS request is completed at time: " + str(datetime.datetime.now().strftime("%Y%m%d %H%M%S")))
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            print("Element appeared on the web page {0}".format(locator))
        except Exception as e:
            print(str(e))
        if element is not None:
            return element

    def wait_for_angular2(self, by_type, locator, timeout = 20):
        element = None
        hasAngularFinishedScript_2 = """
        try {
            //rootSelector - tag contains angular 2 application, feel free to change this urgument 
            rootSelector = 'app'
            el = document.querySelector(rootSelector);
            callback = arguments[arguments.length - 1];
            if (window.getAngularTestability) {
                window.getAngularTestability(el).whenStable(callback('complete'));
            }
            if (window.getAllAngularTestabilities) {
                var testabilities = window.getAllAngularTestabilities();
                var count = testabilities.length;
                var decrement = function() {
                    count--;
                    if (count === 0) {
                        callback('complete');
                        }
                    };
                testabilities.forEach(function(testability) {
                    testability.whenStable(decrement);
                    });
            }
        } catch (err) {
            callback(err.message);
        }  """
        try:
            print("Waiting for maximum :: {0} :: seconds for element :: {1} :: to be clickable {2}".format(str(timeout), locator, str(datetime.datetime.now().strftime("%Y%m%d %H%M%S"))))
            wait = WebDriverWait(self.driver, timeout)
            # res = self.driver.execute_async_script(hasAngularFinishedScript_2)    #debug
            wait.until(lambda driver: self.driver.execute_script("return document.readyState") == "complete")
            wait.until(lambda driver: self.driver.execute_async_script(hasAngularFinishedScript_2)=="complete")
            print("Ajax request is completed at time: " + str(datetime.datetime.now().strftime("%Y%m%d %H%M%S")))
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            #for debud:
            # element = self.driver.find_element(By.XPATH, locator)
            # wait.until(EC.element_to_be_clickable(locator))
            print("Element appeared on the web page {0}".format(locator))
        except Exception as e:
            print("Element isn't appeared on the web page, details:"+str(e))
        if element is not None:
            return element

    def get_title(self):
        return self.driver.title

    def wait_for_allert(self, timeout = 5):
        try:
            print("Waiting for maximum :: {0} :: seconds for alert to be clickable {1}".format(str(timeout), str(datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"))))
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.alert_is_present())
            print("Allert appeared on the web page ")
        except NoAlertPresentException as e:
            print(str(e))

    def wait_for_allert_is_not_present(self, timeout = 5):
        try:
            print("Waiting for maximum :: {0} :: seconds for alert to be clickable {1}".format(str(timeout), str(datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"))))
            wait = WebDriverWait(self.driver, timeout)
            wait.until(self.allert_is_not_present())
            print("Allert appeared on the web page ")
        except NoAlertPresentException as e:
            print(str(e))

    def allert_is_not_present(self):
        try:
            text = self.driver.switch_to.alert.text
            return False
        except NoAlertPresentException:
            return True