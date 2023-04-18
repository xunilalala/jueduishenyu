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
    {'username': 'cuishi', 'password': 'yi-KY.T:qr6iMwy'},
    {'username': 'daishen', 'password': 'miMJhPcv5MA!u!w'},
    {'username': 'quechao', 'password': 't5W2Sw5vrH:X6A-'},
    {'username': 'songhao', 'password': 'TZd!FXrvqSja2b6'},
    {'username': 'tianshu', 'password': 'R!234n-bs3.anQD'},
    {'username': 'xuni', 'password': 'AdfG:CaufU6inec'},
    {'username': 'yituodabian', 'password': '2Ncx-sm_8jefX7r'},
    {'username': 'licheng', 'password': '-m-eeDki8x8CprT'}
]

for user in users:
    # 创建Chrome浏览器对象
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # 打开网页

    # 打开网页
    driver.get('https://www.sdhhz.cc/')
    # 点击登录按钮
    time.sleep(10)
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'empty')))
    login_button.click()
    time.sleep(5)
    # 在登录页面中输入用户名和密码并点击登录按钮
    username = driver.find_element_by_name("username")
    username.send_keys(user['username'])
    password = driver.find_element_by_name("password")
    password.send_keys(user['password'])
    print(f"Logging in as {user['username']}")
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="快速登录"]')))
    login_button.click()
    time.sleep(8)
    # 点击今日签到
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="bar-item bar-mission"]')))
    sign_in_button.click()
    # 点击领取签到奖励
    time.sleep(3)
    reward_button_list = driver.find_elements_by_xpath('//div[@class="bar-user-info-row bar-mission-action"]')
    if len(reward_button_list) > 0:
        reward_button = reward_button_list[0]
        reward_button.click()
    else:
        print('Element not found')


    # 关闭浏览器
    driver.quit()
    time.sleep(10)
    print(user['username']+"完成签到")
print("神代--完成")
