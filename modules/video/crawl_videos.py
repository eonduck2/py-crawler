from selenium.webdriver.common.by import By

def crawl_videos(driver, setter):
    videos = driver.find_elements(By.CSS_SELECTOR, 'ytd-video-renderer')
    new_videos_found = False
    
    for video in videos:
        try:
            video_title = video.find_element(By.CSS_SELECTOR, '#video-title').get_attribute('title')
            views = video.find_element(By.CSS_SELECTOR, '#metadata-line span:nth-of-type(1)').text
            upload_date = video.find_element(By.CSS_SELECTOR, '#metadata-line span:nth-of-type(2)').text
            channel_name = video.find_element(By.CSS_SELECTOR, '#text-container a:nth-of-type(1)').get_attribute('innerText')

            
            if video_title not in setter:
                setter.add(video_title)
                print(f"새 동영상 제목: {video_title}")
                print(f"조회수: {views}")
                print(f"업로드 날짜: {upload_date}")
                print(f"채널 이름: {channel_name}")
                new_videos_found = True
        except Exception as e:
            print(f"정보 추출 오류: {e}")
    
    return new_videos_found