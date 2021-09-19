
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from Settings.headless_setting import *
from Settings.selenium_setting import *

# 페이스북 로그인 페이지 가져오기
driver.get("https://www.facebook.com/")

user_name = "아이디"
password = "비밀번호"
email_id = "//*[@id='email']"
password_id = "//*[@id='pass']"
login_button = "//*[@name='login']"

email_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, email_id)))
password_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, password_id)))
login_button_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_button)))

email_tag.clear()
email_tag.send_keys(user_name)
password_tag.clear()
password_tag.send_keys(password)
login_button_tag.click()

driver.quit()

