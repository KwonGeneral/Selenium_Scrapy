
from Settings.headless_setting import *

# 크롤링 사이트 설정
driver.get("https://news.v.daum.net/v/20210918210509562")

# 뉴스 '메뉴' 가져오기
# nav = driver.find_element_by_css_selector("div[role]")
nav = driver.find_element_by_css_selector("div[role='navigation']")
print("다음 뉴스 메뉴 : ", nav.text)

# 뉴스 '헤더 제목' 가져오기
header_title = driver.find_element_by_css_selector("head > title")
print("뉴스 헤더 제목 : ", header_title.get_attribute("text"))

# 뉴스 '제목' 가져오기
title = driver.find_element_by_class_name("tit_view")
print("뉴스 제목 : ", title.text)

# 뉴스 '내용' 가져오기
content = driver.find_element_by_id("harmonyContainer")
print("뉴스 내용 : ", content.text)

# 드라이버 종료
driver.quit()

