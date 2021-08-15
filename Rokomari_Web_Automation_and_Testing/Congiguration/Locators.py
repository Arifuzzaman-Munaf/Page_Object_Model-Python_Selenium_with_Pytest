"""This class carries all the locators that we have to use for
automation and testing"""
from selenium.webdriver.common.by import By

class Locators :
    sign_in_navigator = (By.CSS_SELECTOR, ".logged-out-user-menu-btn")  # by css selector
    email = (By.XPATH, "//input[@id='j_username']")  # by XPath
    password = (By.XPATH, "//input[@id='j_password']")  # by XPath
    sign_in_button = (By.XPATH, "/html/body/header/div/div/div/div/div[3]/div/div[2]/div/form/button")  # by XPath

