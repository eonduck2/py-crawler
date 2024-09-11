import modules
import modules.browser_treader
import modules.check
import modules.check.result_checker
import modules.driver
import modules.driver.get_driver
import modules.json
import modules.json.file_name_generator
import modules.settings
import modules.settings.crawl_setter
import modules.url
import modules.url.query_generator
import modules.video
import modules.video.crawl_videos 
import static
import static.tarantula_static
import os

input_data = input(static.tarantula_static.system_input_title)
url = modules.url.query_generator.query_generator(input_data)

driver = modules.driver.get_driver.get_driver()

driver.get(url)

title = driver.title
print(static.tarantula_static.youtube_title_prefix_message, title)

crawled_videos = modules.settings.crawl_setter.crawl_setter()
video_data = []


file_path = os.path.join(static.tarantula_static.save_folder_path, modules.json.file_name_generator.generate_file_name(input_data))

try:
    while True:
        if not modules.video.crawl_videos.crawl_videos(driver, crawled_videos, video_data, file_path):
            modules.browser_treader.browser_treader(driver)

        if modules.check.result_checker.result_checker(driver):
            print(static.tarantula_static.no_more_result_kill_task_message)
            break

except KeyboardInterrupt:
    print(static.tarantula_static.kill_task_crawling_message)
finally:
    driver.quit()