from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import modules
import modules.options
import modules.options.get_options


def get_driver(headless=False):
    options = modules.options.get_options.sele_options_getter()
    if headless:
        options.headless = True  # headless 모드를 사용할 경우

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver