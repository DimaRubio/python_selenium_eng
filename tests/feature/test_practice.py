from common.base_test import BaseTest
import pytest
import allure

from pages.page_manager import PageManager
from pages.page_for_practice import PracticePage


class TestClass1:

    def test_1_1(self, driver_set_up):
        driver_set_up.instance.get('http://lessons2.ru/python-for-testers/')

    @pytest.mark.skip
    def test_1_2(self, driver_set_up):
        driver_set_up.instance.get('http://automated-testing.info')


class TestClass2:

    def test_2_1(self, driver_set_up):
        driver_set_up.instance.get('http://lessons2.ru/')

    @pytest.mark.skip
    def test_2_2(self, driver_set_up):
        driver_set_up.instance.get('http://twitter.com/autotestinfo')


@pytest.mark.usefixtures("classSetup")
@allure.feature("Test class for practice")
class TestClassExample:

    @pytest.fixture(scope="class")
    def classSetup(self, request, driver_set_up):
        driver = driver_set_up.instance
        pagePractice = PracticePage(driver)
        if request.cls is not None:
            request.cls.pagePractice = pagePractice
        yield

    @allure.story("Dou Example")
    def test_3_1(self):
        self.pagePractice.goTo('https://dou.ua/')
        self.pagePractice.clickForumButoon()

    @allure.story("AngularJS example")
    def test_3_2(self):
        self.pagePractice.goTo('https://www.oppia.org/splash')
        self.pagePractice.click_on_Angular()

    @allure.story("Angular 2 example")
    def test_3_3(self):
        self.pagePractice.goTo('http://localhost:8181/#/login')
        self.pagePractice.click_on_Angular2()
