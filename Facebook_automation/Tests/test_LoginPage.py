import pytest

from Facebook_automation_and_testing.Config.config import TestData
from Facebook_automation_and_testing.Tests.test_base import BaseTest
from Facebook_automation_and_testing.pages.LoginPage import LoginPage

"""This class is inherited from BaseTest class as a fixture"""


class TestLogin(BaseTest):

    """this method tests whether create account link is working or not"""
    def test_create_account_link_visible(self):
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.is_link_visible()
        assert flag, "The link is not visible"

    """This methods checks the title of the page is okay or not"""
    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.get_login_page_title() == TestData.page_title

    """This method tests for login accessibility"""
    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.email, TestData.password)
