from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()

def get_driver(headless=False):
    options = Options()
    if headless:
        options.headless = True  # headless 모드를 사용할 경우

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver