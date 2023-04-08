from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)

# 访问网址
driver.get("https://studiolab.sagemaker.aws/")

# 等待页面加载完成
time.sleep(20)

# 模拟点击登录按钮
button = driver.find_element_by_xpath("//button[contains(., 'Sign in')]")
button.click()

# 等待2秒后输入用户名和密码，然后点击登录按钮
time.sleep(2)
username_input = driver.find_element_by_name("username")
username_input.send_keys("xuni1024")

password_input = driver.find_element_by_name("password")
password_input.send_keys("ml,152ml.636")

submit_button = driver.find_element_by_xpath("//button[contains(@class, 'qa-signin-submit-button')]")
submit_button.click()

# 等待页面加载完成
time.sleep(20)

# 点击Start runtime按钮
start_button = driver.find_element_by_xpath('//button[@class="MuiButtonBase-root MuiButton-root qa-start-stop-button css-1sncjuj MuiButton-text"]')
start_button.click()

# 等待20秒
time.sleep(20)

# 点击Open project按钮
project_button = driver.find_element_by_xpath('//button[@class="MuiButtonBase-root MuiButton-root qa-launch-project-button css-fbh5z4 MuiButton-text Mui-disabled Mui-disabled"]')
project_button.click()

# 关闭浏览器驱动程序
driver.quit()
