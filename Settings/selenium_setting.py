
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 크롬드라이버 설정
chd = 'C:/dev_files/chd/chd.exe'
driver = webdriver.Chrome(chd)

# 크롤링할 사이트 호출
# driver.get("https://kwonputer.com")
# driver.get("https://www.python.org/")

# 셀레니움은 웹테스트를 위한 프레임워크로 다음과 같은 방식으로 웹테스트를 자동으로 진행함
# 아래의 내용이 없으면 프로그램 종료
# assert "찾을 내용" in driver.title

