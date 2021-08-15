import pytest

from Rokomari_Web_Automation_and_Testing.Congiguration.config import TestData
from Rokomari_Web_Automation_and_Testing.Pages.LoginPage import LoginPage
from Rokomari_Web_Automation_and_Testing.Tests.test_BasePage import BaseTest

"""This class is inherited from BaseTest class as a fixture"""


class TestLogin(BaseTest):

    """This method tests for login accessibility"""
    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.email, TestData.password)
        if len(TestData.email)==0 and len(TestData.email)==0:
            assert False
