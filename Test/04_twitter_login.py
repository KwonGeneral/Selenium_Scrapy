
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Settings.selenium_setting import *

# 트위터 로그인 페이지 가져오기
driver.get("http://www.twitter.com")

login_link = "//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span"
login_link_tag = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, login_link)))
login_link_tag.click()

login_link2 = "//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/a"
login_link2_tag = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, login_link2)))
login_link2_tag.click()

user_name = "아이디"
password = "비밀번호"
email_id = "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input"
password_id = "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input"
login_btn_id = "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div"

email_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, email_id)))
password_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, password_id)))
login_btn_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_btn_id)))

email_tag.clear()
email_tag.send_keys(user_name)
password_tag.clear()
password_tag.send_keys(password)
login_btn_tag.click()

# driver.quit()

