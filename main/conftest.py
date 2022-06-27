import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope='class')
def setup(request):
    # Setup for Chrome Driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-error')
    s = Service("C:\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=chrome_options)

    # Maximizing the window
    driver.maximize_window()

    # Opening the website
    driver.get('https://www.gmail.com/')

    request.cls.driver = driver
    yield
    driver.close()


