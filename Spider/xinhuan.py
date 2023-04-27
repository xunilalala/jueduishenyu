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


# 用户名密码表
users = [
    
    {'username': '3120294679@qq.com', 'password': 'ml152636'},
    {'username': '18264410349@163.com', 'password': 'SWNNnq:mi5L6bHT'},
    {'username': 'wanzhanadmin@163.com', 'password': 'zwD2!D_PhnSWpYR'},
    {'username': 'xiajibaluanxiede@163.com', 'password': '-K42!FycASxT3mS'}
]

for user in users:
    # 创建Chrome浏览器对象
    driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)
    driver.maximize_window()
    # 打开网页

    # 打开网页
    driver.get('https://xhcy.us/author/')
    # 点击登录按钮
    time.sleep(10)
    close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.poi-dialog__header__close")))
    close_button.click()
    # 定位到需要点击的元素
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.inn-sign__login-btn__container a.inn-sign__login-btn")))
    driver.execute_script("arguments[0].click();", login_button)
    # 在登录页面中输入用户名和密码并点击登录按钮
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='pwd']")))
    email_input.send_keys(user['username'])
    password_input.send_keys(user['password'])
    print(f"Logging in as {user['username']}")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();",login_button)
    close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'poi-dialog__footer__btn_default') and text()='关闭']")))
    driver.execute_script("arguments[0].click();", close_button)
    # 点击签到
    signin_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'inn-nav__point-sign-daily__btn') and @title='签到']")))
    signin_button.click()
    # 关闭浏览器
    time.sleep(2)
    driver.quit()
    print(user['username']+"完成签到")
    
print("芯幻--完成")
