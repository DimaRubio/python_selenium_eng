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

    def getEmailField(self):
        return  self.waitForElement(By.XPATH, self._email_field)

    def getPasswordField(self):
        return  self.waitForElement(By.XPATH, self._password_field)

    def click_on_element_by_xpath(self, locator):
        self.driver.execute_script("element = document.evaluate(\"" + locator + "\", document, null, XPathResult.ANY_TYPE, null).iterateNext();if (element !== null) {element.click();};")

    def logInOnSite(self, login, password):
        self.logOut()
        self.goTo('https://dev.mytefl.com/lp-profile/')
        self.getEmailField().send_keys(login)
        self.getPasswordField().send_keys(password)
        self.click_on_element_by_xpath(self._login_button)
        assert  self.get_admin_bar() is not None
