from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scroll_down():
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")