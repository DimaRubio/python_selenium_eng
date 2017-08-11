from common.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _email_field = "//input[@id='user_login']"
    _password_field = "//input[@id='user_pass']"
    _login_button = "//input[@id='wp-submit']"
    _button_up = "//div[@class='footer__sub-btn hide-on-med-only']"
    _menu_mobile = "//ul[contains(@class,'nav-bar__menu-list_mobile')]"
    _menu = "//ul[@class='nav-bar__menu-list']"

    def get_email_field(self):
        return  self.wait_for_element(By.XPATH, self._email_field)

    def get_password_field(self):
        return  self.wait_for_element(By.XPATH, self._password_field)

    # def click_on_element_by_xpath(self, locator):
    #     self.driver.execute_script("element = document.evaluate(\"" + locator + "\", document, null, XPathResult.ANY_TYPE, null).iterateNext();if (element !== null) {element.click();};")

    def logIn_on_site(self, login, password):
        self.delete_cookie()
        self.go_to('https://dev.mytefl.com/lp-profile/')
        self.get_email_field().send_keys(login)
        self.get_password_field().send_keys(password)
        self.wait_for_element(By.XPATH, self._login_button)
        self.click_on_element_by_xpath(self._login_button)
        assert  self.get_dashboard_button() is not None


