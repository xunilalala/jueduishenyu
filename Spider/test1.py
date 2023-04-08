from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
import ddddocr
import requests

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)

# 访问网页
driver.get("http://3xacg.com/user-2")
print("开启，等待登录ing")
# 等待登录框出现
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
print("开始查找")
# 输入账户和密码并登录
username = driver.find_element_by_name("username")
username.send_keys("xuni2048")
password = driver.find_element_by_name("password")
password.send_keys("ml152636")
driver.find_element_by_xpath("//span[@class='captcha-clk2' and text()='显示验证码']").click()
captcha_img = driver.find_element_by_xpath("//span[@class='captcha-clk2']/img").get_attribute("src")
print(captcha_img)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
code_url="http://3xacg.com/wp-content/themes/modown/action/captcha2.php?0.8057091778294176"
r=requests.get(url=code_url,headers=headers,timeout=5)
with open('code.png','wb')as f:
    f.write(r.content)
    print("下载验证码成功！")
 
ocr = ddddocr.DdddOcr()
 
#with open(r'C:\Users\Administrator\Desktop\验证码识别\code.png', 'rb') as f:
    #img_bytes = f.read()
img_bytes=r.content
 
res = ocr.classification(img_bytes)
input_element = driver.find_element_by_id("captcha")

# 向输入框中填写内容
input_element.send_keys(res)
print("填写验证码")
submit_button = driver.find_element_by_xpath("//input[@class='submit login-loader btn']")
submit_button.click()
print(res)
print("完成登录")
time.sleep(30)
element = driver.find_element_by_xpath("//a[@class='usercheck active']")
print("点击元素ing")
# 点击元素
element.click()
driver.quit()
print("OK")
