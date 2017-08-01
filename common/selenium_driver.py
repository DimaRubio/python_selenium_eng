import datetime
import os
from traceback import print_stack

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging


class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by_type, locator, timeout = 20):
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
        except Exception as e:
            print(str(e))
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
            print(str(e))
        if element is not None:
            return element

    def get_title(self):
        return self.driver.title


