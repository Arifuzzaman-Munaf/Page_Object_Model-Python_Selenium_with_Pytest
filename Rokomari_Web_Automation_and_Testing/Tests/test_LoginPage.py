import time

import pytest,allure

from Rokomari_Web_Automation_and_Testing.Congiguration.config import TestData
from Rokomari_Web_Automation_and_Testing.Pages.LoginPage import LoginPage
from Rokomari_Web_Automation_and_Testing.Tests.test_BasePage import BaseTest

"""This class is inherited from BaseTest class as a fixture"""


@allure.severity(allure.severity_level.NORMAL)
class TestLogin(BaseTest):

    """This method tests for login accessibility"""
    def test_login_case1(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.email_case1, TestData.password_case1)
        time.sleep(2)

    def test_login_case2(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.email_case2, TestData.password_case2)
        time.sleep(2)

    def test_login_case3(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.email_case3, TestData.password_case3)
        time.sleep(2)

    def test_login_case4(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.email_case4, TestData.password_case4)
        time.sleep(2)

    def test_login_case5(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.email_case5, TestData.password_case5)
        time.sleep(2)
        self.login_page.screenshot("TestFailedScreenShot")
        if len(TestData.email_case5) == 0 and len(TestData.password_case5) == 0:
            assert False
