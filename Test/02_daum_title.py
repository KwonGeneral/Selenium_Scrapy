
from Settings.headless_setting import *

# 크롤링 사이트 설정
driver.get("https://news.v.daum.net/v/20210918210509562")

# 최초 발견한 태그만 검색
title = driver.find_element_by_tag_name("h3")
print(title)

# 모든 태그 검색
h3s = driver.find_elements_by_tag_name("h3")
for h3 in h3s:
    print(h3.text)

# 드라이버 종료
driver.quit()