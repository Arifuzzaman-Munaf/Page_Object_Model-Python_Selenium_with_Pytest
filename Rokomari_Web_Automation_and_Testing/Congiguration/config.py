"""This class caries all the keys and details which we want to execute
in this project"""


class TestData:
    BaseUrl = "https://www.rokomari.com/book"
    executable_path = "F:\\GitHub\\WebDrivers\\geckodriver"
    email_case1 = email_case2 = "arifuzzamanmunaf@gmail.com"
    password_case1 = password_case3 = "Rokomari@Munaf"

    password_case4 = password_case2 = "12345678"
    email_case4 = email_case3 = "xyz@gmail.com"

    email_case5 = password_case5 = ""

# from selenium.webdriver.common.by import By
# import time
# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.support.ui import Select
#
#
# # installing Firefox driver manager for executing webdriver for further process
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver.implicitly_wait(3)
#
#
# # Visiting the webpage mentioned in the URL
# driver.get("https://www.rokomari.com/book")
#
# # print the title of page
# print(driver.title)
#
# sign_in_navigator = driver.find_element(By.CSS_SELECTOR, ".logged-out-user-menu-btn")
# sign_in_navigator.click()
#
# email = driver.find_element(By.XPATH, "//input[@id='j_username']")
# password = driver.find_element(By.XPATH, "//input[@id='j_password']")
# sign_in_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div[2]/div[2]/form/button")
#
# email.send_keys('arifuzzamanmunaf@gmail.com')
# password.send_keys('Rokomari@Munaf')
# sign_in_button.click()
