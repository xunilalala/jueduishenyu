from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
import random
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)


# 设置固定等待时间为10秒
FIXED_WAIT_TIME = 10

driver.get("https://studiolab.sagemaker.aws/login")
time.sleep(FIXED_WAIT_TIME + random.randint(120, 160))

# 输入账号密码，点击登录
username_field = driver.find_element_by_name("username")
username_field.clear()
username_field.send_keys("xuni1024")

password_field = driver.find_element_by_name("password")
password_field.clear()
password_field.send_keys("ml,152ml.636")

login_button = driver.find_element_by_xpath("//button[contains(@class, 'qa-signin-submit-button')]")
login_button.click()
time.sleep(20 + random.randint(10, 20))

# 启动运行时
start_button = driver.find_element_by_xpath("//button[contains(@class, 'qa-start-stop-button')]")
start_button.click()
time.sleep(20 + random.randint(10, 20))


# 启动运行时
start_button = driver.find_element_by_xpath("//button[contains(@class, 'qa-start-stop-button')]")
start_button.click()
time.sleep(FIXED_WAIT_TIME + random.randint(10, 20))

# 点击打开项目
open_project_button = driver.find_element_by_xpath("//button[contains(@class, 'qa-launch-project-button')]")
open_project_button.click()
time.sleep(FIXED_WAIT_TIME + random.randint(10, 20))

# 关闭浏览器
driver.quit()
