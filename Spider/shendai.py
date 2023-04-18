from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-setuid-sandbox')
chrome_options.add_argument('--no-first-run')
chrome_options.add_argument('--no-zygote')
chrome_options.add_argument('--single-process')
chrome_options.add_argument('--headless')

# 创建Chrome浏览器对象
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
# 打开网页
driver.get('https://www.sdhhz.cc/')

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
    # 点击登录按钮
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'empty')))
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
    
    try:
        reward_button.click()
    except: print(user['username']+"可能签到失败")
    # 关闭浏览器
    driver.quit()

print("所有用户签到完成")
