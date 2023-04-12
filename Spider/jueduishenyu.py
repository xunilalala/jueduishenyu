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

users = [
    {'username': 'xuni512', 'password': 'ml,152ml.636'},
    {'username': 'xuni', 'password': 'ml,152ml.636'},
    {'username': 'xuni1024', 'password': 'ml,152ml.636'},
    {'username': 'xuni256', 'password': 'ml,152ml.636'},
    {'username': 'xuni2048', 'password': '592uir4UdtqGn3!'}
]

for user in users:
    driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)

    # 访问网页
    driver.get("http://www.acg088.com/user/coin")

    # 等待登录框出现
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    # 输入账户和密码并登录
    username = driver.find_element_by_name("username")
    username.send_keys(user['username'])
    password = driver.find_element_by_name("password")
    password.send_keys(user['password'])
    driver.find_element_by_class_name("go-login").click()
    print(f"{user['username']}完成登录")

    time.sleep(10)
    # 等待关闭按钮出现

    WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.CLASS_NAME, "swal2-close")))
    driver.execute_script("document.querySelector('.swal2-close').click()")

    # 等待签到按钮出现并点击
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "go-user-qiandao"))
    )
    driver.find_element_by_class_name("go-user-qiandao").click()
    time.sleep(10)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "go-user-qiandao"))
    )
    driver.find_element_by_class_name("go-user-qiandao").click()
    driver.quit()
    print(f"{user['username']}签到完成")

print("所有用户签到完成")
