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
    {'username': '3120294679@qq.com', 'password': 'nT!LKsZh8P4:w-w'}
]

for user in users:
    # 创建Chrome浏览器对象
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # 打开网页

    # 打开网页
    driver.get('https://www.yuzhaiwuyu.com/')
    # 点击登录按钮
    time.sleep(10)
   
    # 创建 ActionChains 对象
    actions = ActionChains(driver)

    # 定位到需要点击的元素
    login_button = driver.find_element_by_xpath("//button[@class='empty mobile-hidden']")
    
    # 将鼠标移动到元素位置
    actions.move_to_element(login_button).perform()

    # 等待一段时间，让被遮挡的元素消失
    time.sleep(1)

    # 再次点击元素
    login_button.click()
    # 在登录页面中输入用户名和密码并点击登录按钮
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
    username_input.send_keys(user['username'])
    password_input.send_keys(user['password'])
    print(f"Logging in as {user['username']}")
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="快速登录"]')))
    login_button.click()
    time.sleep(8)
    # 点击今日签到
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="bar-item bar-mission"]')))
    sign_in_button.click()
    # 点击领取签到奖励
    time.sleep(3)
    reward_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="bar-user-info-row bar-mission-action"]')))
    reward_button.click()
    # 关闭浏览器
    driver.quit()
    time.sleep(10)
    print(user['username']+"完成签到")
print("御宅--完成")
