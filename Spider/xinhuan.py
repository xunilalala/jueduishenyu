from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 创建谷歌浏览器options对象，设置一些参数
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
chromedriver = "/usr/bin/chromedriver"
# 创建浏览器对象
browser = webdriver.Chrome(options=option,executable_path=chromedriver)

# 将webdriver属性置为undefined
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})

# 窗口最大化
browser.maximize_window()

# 访问网址 https://xhcy.us/
start_time = time.time()  # 记录开始运行时间
browser.get("https://xhcy.us/")

# 显示等待，等待关闭按钮出现
close_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.poi-dialog__footer__btn")))

# 点击关闭按钮
close_button.click()

# 显示等待，等待登录按钮出现
login_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "inn-sign__login-btn")))

# 点击登录按钮
login_button.click()

# 显示等待，等待邮箱输入框出现
email_input = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "email")))

# 输入邮箱
email_input.send_keys("xiangz91121i@163.com")

# 显示等待，等待密码输入框出现
password_input = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "pwd")))

# 输入密码
password_input.send_keys("4_v8mee73RdRNrH")

# 显示等待，等待登录按钮出现
submit_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.poi-dialog__footer__btn_success")))

# 点击登录按钮
submit_button.click()

# 显示等待，等待关闭按钮出现
close_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.poi-dialog__footer__btn")))

# 点击关闭按钮
close_button.click()

wait = WebDriverWait(browser, 10)
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inn-nav__point-sign-daily a')))
button.click()

# 显示等待，等待关闭按钮出现
close_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.poi-dialog__footer__btn")))

# 点击关闭按钮
close_button.click()

end_time = time.time()  # 记录结束运行时间
print(f"代码执行时间为：{end_time - start_time}秒")

# 关闭浏览器
browser.quit()
