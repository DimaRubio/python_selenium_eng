from pages import *
from common.base_page import BasePage


class PageManager:

    def __init__(self, browser):
        self.base = BasePage(browser)
        self.login = login_page.LoginPage()
        self.select_course = select_course_page.OnlineCoursePage()
        self.check_out = check_out_page.CheckOutPage()
        self.lesson_content = lesson_content_page.LessonContentPage()
        self.quiz_content = quiz_page.QuizContentPage()
        self.lp_courses = lp_courses_page.LPCoursesPage()
        self.profile = profile_page.ProfilePage()
