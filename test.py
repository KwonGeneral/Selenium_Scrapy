
# from settings.selenium_setting import *
from settings.phantom_setting import *

print(driver.current_url)
print(driver.title)
print("??")

elem = driver.find_element_by_name("q")

# input 텍스트 초기화
elem.clear()

# 키 이벤트 전송
elem.send_keys("python")

# 엔터 입력
elem.send_keys(Keys.RETURN)

time.sleep(2)

assert "No results found." not in driver.page_source

driver.quit()

