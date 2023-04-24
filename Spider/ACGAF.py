from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')



# 用户名密码表
users = [
    {'username': '18264410349@163.com', 'password': 'vBKH%SDFHasd.'},
    {'username': '3120294679@qq.com', 'password': 'vBKH!:nfNv8vkC.'}
]

for user in users:
    # 创建Chrome浏览器对象
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # 打开网页

    # 打开网页
    driver.get('https://www.acgaf.gay/')
    # 点击登录按钮
    time.sleep(10)
   
   
    # 定位到需要点击的元素
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'empty')))
    driver.execute_script("arguments[0].click();", login_button)
    # 在登录页面中输入用户名和密码并点击登录按钮
    time.sleep(5)
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
    time.sleep(5)
    username_input.send_keys(user['username'])
    password_input.send_keys(user['password'])
    print(f"Logging in as {user['username']}")
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="快速登录"]')))
    login_button.click()
    time.sleep(5)
    # 点击今日签到
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="bar-item bar-mission"]')))
    sign_in_button.click()
    # 点击领取签到奖励
    time.sleep(3)
    reward_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="bar-user-info-row bar-mission-action"]')))
    driver.execute_script("arguments[0].click();", reward_button)
    # 关闭浏览器
    time.sleep(2)
    driver.quit()
    print(user['username']+"完成签到")
    
print("ACGAF--完成")
