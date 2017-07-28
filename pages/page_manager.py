from pages.login_page import *
from pages.online_course_page import *
from pages.check_out_page import *


class PageManager:

    def __init__(self, driver):
        self.driver = driver
        self.login = LoginPage(driver)
        self.online_course = OnlineCoursePage(driver)
        self.check_out = CheckOutPage(driver)