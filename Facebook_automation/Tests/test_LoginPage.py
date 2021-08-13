import pytest

from Facebook_automation.Tests.test_base import BaseTest
from Facebook_automation.pages.LoginPage import LoginPage

"""This class is inherited from BaseTest class as a fixture"""


class TestLogin(BaseTest):

    """this method tests whether create account link is working or not"""
    def create_account_link_visible(self):
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.is_link_visible()