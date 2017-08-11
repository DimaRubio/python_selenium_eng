# from pages.login_page import *
# from pages.select_course_page import *
# from pages.check_out_page import *
# from pages.lesson_content_page import *
from pages import *


class PageManager:

    def __init__(self, driver):
        self.driver = driver
        self.login = login_page.LoginPage(driver)
        self.select_course = select_course_page.OnlineCoursePage(driver)
        self.check_out = check_out_page.CheckOutPage(driver)
        self.lesson_content = lesson_content_page.LessonContentPage(driver)
        self.quiz_content = quiz_page.QuizContentPage(driver)
        self.lp_courses = lp_courses_page.LPCoursesPage(driver)