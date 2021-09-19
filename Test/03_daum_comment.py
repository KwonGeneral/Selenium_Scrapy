
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 특정 태그 존재 여부 확인 : (By.ID, "alex-area")
from selenium.webdriver.common.by import By

from Settings.selenium_setting import *

# 크롤링 사이트 설정
driver.get("https://news.v.daum.net/v/20170202180355822")

# 더 보기 버튼이 있는지 확인하기 위한 변수
loop, count = True, 0

while loop and count < 10:
    try:
        element = WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "#alex-area > div > div > div > div.cmt_box > div.alex_more > button")
            )
        )
        more_button = driver.find_element_by_css_selector("#alex-area > div > div > div > div.cmt_box > div.alex_more > button")
        webdriver.ActionChains(driver).click(more_button).perform()
        count += 1
        time.sleep(2)
    except TimeoutException:
        loop = False


comment_box = driver.find_element_by_css_selector("#alex-area > div > div > div > div.cmt_box > ul.list_comment")
comment_list = comment_box.find_elements_by_tag_name("li")

for index, item in enumerate(comment_list):
    print("[ ", index, "번째 ] 댓글 내용 : ", item.find_element_by_css_selector("div p").text)

driver.quit()



# 특정 태그 일정 시간 기다리기 1)
# element = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.ID, "alex-area")))

# 특정 태그 일정 시간 기다리기 2)
# try:
#     element = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "a")))
#     more_button = driver.find_element_by_css_selector("a")
#     more_button.click()
# except TimeoutException:
#     loop = False

# 특정 태그 일정 시간 기다리기 3)
# try:
#     element = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.ID, "cMain")))
# except TimeoutException:
#     print("Error : TimeoutException")
# finally:
#     driver.quit()

# 키보드 / 마우스 동작 자동화 1)
# hidden_subment = driver.find_element_by_css_selector(".nav #submenu1")
# actions = webdriver.ActionChains(driver)
# actions.click(hidden_subment)
# actions.perform()

# 키보드 / 마우스 동작 자동화 2)
# webdriver.ActionChains(driver).click(hidden_subment).perform()

