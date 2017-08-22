import datetime
import os
from traceback import print_stack
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
from utilities.util import Util


class SelenDriver:
    __instance = None

    def __new__(cls, browser_type):
        if SelenDriver.__instance is None:
            SelenDriver.__instance = object.__new__(cls)
            if browser_type == "firefox":
                SelenDriver.__instance.driver = webdriver.Firefox()
            else:
                SelenDriver.__instance.driver = webdriver.Chrome()
            SelenDriver.__instance.driver.implicitly_wait(10)
            SelenDriver.__instance.driver.set_script_timeout(10)
            SelenDriver.__instance.driver.maximize_window()
        return SelenDriver.__instance







