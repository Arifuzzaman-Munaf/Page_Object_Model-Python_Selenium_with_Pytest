
# all the libraries that we need for automation and testing
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
import allure

"""This class is the parent class of all pages
It contains all the common methods and utilities for other page classes"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    """this method deals with clicking operation for any element"""
    def do_click(self, locator):
        WebDriverWait(self.driver, 10).until(exp.visibility_of_element_located(locator)).click()

    """This method is used for sending information to the website"""
    def do_send_keys(self, locator, text):
         WebDriverWait(self.driver, 10).until(exp.visibility_of_element_located(locator)).send_keys(text)

    # """this method helps to hover elements"""
    # def do_hover_elements(self, locator):
    #     hover = ActionChains(self.driver)
    #     action = WebDriverWait(self.driver, 10).until(exp.visibility_of_element_located(locator))
    #     hover.move_to_element(action).perform()

    def get_screenshot(self):
        allure.attach()




