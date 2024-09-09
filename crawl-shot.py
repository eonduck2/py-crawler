from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'http://books.toscrape.com'
driver.get(url)

title = driver.title
print(f"페이지 제목: {title}")

books = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod')
for book in books:
    title = book.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
    price = book.find_element(By.CSS_SELECTOR, 'p.price_color').text
    print(f"책 제목: {title} - 가격: {price}")

driver.quit()
