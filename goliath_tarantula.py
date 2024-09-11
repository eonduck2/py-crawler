from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import modules 

options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

data = "음식"

url = f'https://www.youtube.com/results?search_query={data}'
driver.get(url)

title = driver.title
print(f"페이지 제목: {title}")

crawled_videos = set()

def scroll_down():
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

def crawl_videos():
    videos = driver.find_elements(By.CSS_SELECTOR, 'h3 a#video-title')
    new_videos_found = False
    for video in videos:
        video_title = video.get_attribute('title')
        if video_title not in crawled_videos: 
            crawled_videos.add(video_title)
            print(f"새 동영상 제목: {video_title}")
            new_videos_found = True
    return new_videos_found

def check_no_more_results():
    try:
        no_more_results_element = driver.find_element(By.XPATH, "//*[contains(text(), '결과가 더 이상 없습니다')]")
        return no_more_results_element is not None
    except:
        return False

try:
    while True:
        if not crawl_videos():
            print("새로운 동영상을 찾지 못함. 스크롤을 내립니다.")
        
        scroll_down()

        if check_no_more_results():
            print("결과가 더 이상 없습니다. 크롤링을 종료합니다.")
            break


except KeyboardInterrupt:
    print("크롤링을 중지합니다.")
finally:
    driver.quit()  