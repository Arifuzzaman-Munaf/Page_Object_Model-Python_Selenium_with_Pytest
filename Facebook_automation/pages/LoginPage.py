from selenium.webdriver.common.by import By

from Facebook_automation.Config.config import TestData
from Facebook_automation.pages.BasePage import BasePage


"""creating Login page class for executing automation"""
"""This page inherits BasePage for all the methods it needs"""


class LoginPage(BasePage):

    """All the attributes for Login page"""
    Email = (By.ID, 'email')
    Password = (By.ID, 'pass')
    login_button = (By.XPATH,"//button[@id='u_0_d_VN']")
    create_account_link = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/a')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_Url)

    """All the actions of login page"""
    """This method returns the title of the page"""
    def get_login_page_title(self):
        return self.driver.title

    """this method check if the create account link is visible or not"""
    def is_link_visible(self):
        return self.is_enabled(self.create_account_link)

    """this method helps to login into profile"""
    def do_login(self, username, password):
        self.do_send_keys(self.Email, username)
        self.do_send_keys(self.Password, password)
        self.do_click(self.login_button)

