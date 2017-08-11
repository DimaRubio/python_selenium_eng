import allure
import pytest
from selenium import webdriver
from pages.page_manager import PageManager


""" One way fo run test
"""
class DriverManager(object):

    def __init__(self, browser):
        self._instance = None
        self.browser_type = browser

    def start(self):
        # implement logic to create instance depends on condition
        if self.browser_type == "firefox":
            self._instance = webdriver.Firefox()
        else:
            self._instance = webdriver.Chrome()
        self._instance.implicitly_wait(10)
        self._instance.set_script_timeout(10);
        self._instance.maximize_window()

        return self._instance

    @property
    def instance(self):
        if not self._instance:
            self.start()
        return self._instance

    def stop(self):
        self._instance.close()


@pytest.fixture(scope="session")
def driver_set_up(request, browser, osType):
    driverManager = DriverManager(browser)
    yield driverManager
    driverManager.stop()


@pytest.fixture(scope="class")
def user_admin(request):
    login = "dmytro.bolyachin@extrawest.com"
    password = "pr0st0123456"
    if request.cls is not None:
        request.cls.login = login
        request.cls.password = password

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope="class")
def create_user(request, driver_set_up):
    driver = driver_set_up.instance
    pm = PageManager(driver)

    # pm.login.logIn_on_site("dmytro.bolyachin@extrawest.com","pr0st0123456")
    # pm.login.logIn_on_site("test20170811104838@test.qa","123456") #баг с расчетом процентов

    # pm.login.logIn_on_site("user20170801134255@test.qa","123456")
    # pm.login.logIn_on_site("test20170803164724@test.qa","123456")
    # pm.login.logIn_on_site("test20170807172826@test.qa","123456")
    # pm.login.logIn_on_site("test20170809102650@test.qa","123456")
    # pm.login.logIn_on_site("test20170811163615@test.qa","123456")

    with allure.step("create user"):
        pm.login.delete_cookie()
        pm.login.go_to('https://dev.mytefl.com/online-onsite-courses/online-tefl-courses/')
        with allure.step("select professional course"):
            pm.select_course.click_on_professional_course_button()
        with allure.step("click on enroll course button"):
            pm.select_course.click_on_enroll_button()
        pm.check_out.create_new_user()

    request.cls.pm = pm
