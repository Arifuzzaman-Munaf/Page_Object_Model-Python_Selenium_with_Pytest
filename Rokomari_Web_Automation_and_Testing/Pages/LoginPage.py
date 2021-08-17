from selenium.webdriver.common.by import By
import time
from Rokomari_Web_Automation_and_Testing.Congiguration.Locators import Locators
from Rokomari_Web_Automation_and_Testing.Congiguration.config import TestData
from Rokomari_Web_Automation_and_Testing.Pages.BasePage import BasePage

"""creating Login page class for executing automation"""
"""This page inherits BasePage for all the methods it needs"""


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BaseUrl)

    """All the actions of login page"""
    """This method returns the title of the page"""
    def get_login_page_title(self):
        return self.driver.title

    """this method helps to login into profile"""
    def do_login(self, Email, Password):
        self.do_click(Locators.sign_in_navigator)
        time.sleep(1)
        self.do_send_keys(Locators.email, Email)
        self.do_send_keys(Locators.password, Password)
        time.sleep(1)
        self.do_click(Locators.sign_in_button)

    def screenshot(self, filename):
        self.get_screenshot(filename)

