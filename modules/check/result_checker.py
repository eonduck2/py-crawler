from selenium.webdriver.common.by import By

def result_checker(driver):
    try:
        no_more_results_element = driver.find_element(By.XPATH, "//*[contains(text(), '결과가 더 이상 없습니다')]")
        return no_more_results_element is not None
    except:
        return False