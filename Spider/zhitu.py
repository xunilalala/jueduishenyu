from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
from PIL import Image
import ddddocr

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

users = [
    {'username': 'songhao', 'password': '4XkfeTF_P.iM_2S'},
    {'username': 'xuni', 'password': '.kh9BtH2!nDmk7d'},
    {'username': 'quechao', 'password': 'H5Zx4h:SETxm7tp'}
]

for user in users:
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get('https://www.rabbit2.top/')
    close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='close']")))
    close_button.click()

    login_button = driver.find_element(By.XPATH, "//li[@class='nav-login no']/a[@class='signin-loader']")
    login_button.click()
    user_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='user_login']")))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
    user_input.send_keys(user['username'])
    password_input.send_keys(user['password'])

    while True:
        try:
            form_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sign-in')))
        except:
            break

        captcha_button = driver.find_element(By.XPATH, "//span[@class='captcha-clk2']")
        captcha_button.click()
        captcha_img = driver.find_element(By.XPATH, "//img[@class='captcha-img']")
        time.sleep(1)
        captcha_png = captcha_img.screenshot_as_png
        with open('captcha.png', 'wb') as f:
            f.write(captcha_png)

        captcha = Image.open('captcha.png')

        ocr = ddddocr.DdddOcr()
        with open('captcha.png', 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)

        Captcha_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='user_captcha']")))
        Captcha_input.clear()
        Captcha_input.send_keys(res)
        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='submit']")))
        login_button.click()
        time.sleep(2)

    try:
        checkin_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='day-checkin']")))
        checkin_button.click()
    except:
        pass

    time.sleep(1)
    driver.quit()
