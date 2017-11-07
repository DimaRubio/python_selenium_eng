import allure
import pytest
from selenium import webdriver
from pages.page_manager import PageManager

@pytest.fixture(scope="session")
def page_manager_set_up(browser):
    pm = PageManager(browser)
    yield pm
    pm.login.driver.close()


@pytest.fixture(scope="class")
def user_admin(request):
    login = "test@test.com"
    password = "123456"
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
def create_user(request, page_manager_set_up):
    pm = page_manager_set_up
    with allure.step("create user"):
        pm.login.delete_cookie()
        pm.login.go_to('https://www.url.com')
        with allure.step("select professional course"):
            pm.select_course.click_on_professional_course_button()
        with allure.step("click on enroll course button"):
            pm.select_course.click_on_enroll_button()
        pm.check_out.create_new_user()
    request.cls.pm = pm
