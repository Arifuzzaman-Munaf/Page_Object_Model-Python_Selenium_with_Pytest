"""This class carries all the locators that we have to use for
automation and testing"""


class Locators :
    sign_in_navigator = ".logged-out-user-menu-btn"  # by css selector
    email = "//input[@id='j_username']"  # by XPath
    password = "//input[@id='j_password']"  # by XPath
    sign_in_button = "/html/body/div[3]/div/section/div[2]/div[2]/form/button"  # by XPath

