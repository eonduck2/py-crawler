from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 웹 드라이버 설정
options = Options()
options.headless = True  # 브라우저를 실제로 열지 않고 백그라운드에서 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 크롤링할 URL
url = 'https://www.naver.com'
driver.get(url)

# 로고 이미지 크롤링
try:
    # 로고가 포함된 이미지 요소 찾기 (클래스명은 실제 페이지의 HTML 구조를 기반으로 설정)
    logo_element = driver.find_element(By.CSS_SELECTOR, 'div#newsstand')  # 클래스명은 실제 HTML 구조를 기반으로 수정
    logo_url = logo_element.get_attribute('src')
    print(logo_element.aria_role)
    
    print(f"로고 이미지 URL: {logo_url}")
except Exception as e:
    print(f"오류 발생: {e}")

# 브라우저 닫기
driver.quit()
