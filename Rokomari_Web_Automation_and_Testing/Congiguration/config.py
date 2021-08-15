"""This class caries all the keys and details which we want to execute
in this project"""
class TestData:
    BaseUrl = "https://www.rokomari.com/book"
    executable_path = "F:\\GitHub\\WebDrivers\\geckodriver"
    email ="arifuzzamanmunaf@gmail.com"
    password = "Rokomari@Password"

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
