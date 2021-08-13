import pytest
from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager


from Facebook_automation_and_testing.Config.config import TestData

# decorator to create modified fixtures with parameters having the scope class


@pytest.fixture(params=['chrome', 'firefox'],scope='class')
def init_driver(request):

    # request.param is helping us to overcome the redundancy of writing separate
    # code blocks for different browser
    # when the parameter is 'chrome' we will install the driver of edge browser
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path=TestData.Chrome_executable_path)

    # when the parameter is 'firefox' we will install the driver of Firefox browser
    if request.param == 'firefox' :
        web_driver = webdriver.Firefox(executable_path=TestData.FireFox_executable_path)

    request.cls.driver = web_driver

    yield
    web_driver.close()