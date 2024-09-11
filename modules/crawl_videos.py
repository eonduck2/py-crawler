from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

crawled_videos = set()

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