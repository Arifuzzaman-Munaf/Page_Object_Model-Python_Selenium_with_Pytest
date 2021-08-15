import pytest, time
from selenium import webdriver


# decorator to create modified fixtures with parameters having the scope class
from Rokomari_Web_Automation_and_Testing.Congiguration.config import TestData


@pytest.fixture(params=['firefox'], scope='class')
def init_driver(request):

    # request.param is helping us to overcome the redundancy of writing separate
    # code blocks for different browser
    # when the parameter is 'firefox' we will install the driver of Firefox browser
    if request.param == 'firefox' :
        web_driver = webdriver.Firefox(executable_path=TestData.executable_path)

    request.cls.driver = web_driver

    yield
    time.sleep(3)
    web_driver.close()