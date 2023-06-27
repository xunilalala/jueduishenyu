
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# 创建谷歌浏览器options对象，设置一些参数
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
option.add_argument('--headless')
chromedriver = "/usr/bin/chromedriver"

# 多个用户登录信息
users = [
    {'email': '18264410349@163.com', 'password': 'SWNNnq:mi5L6bHT'},
    {'email': '3120294679@qq.com', 'password': 'ml152636'},
    {'email': 'chengxinchengyi@163.com', 'password': '5hRc.49smV!rq.y'},
    {'email': 'wanzhanadmin@163.com', 'password': 'zwD2!D_PhnSWpYR'},
    {'email': 'xiangz91121i@163.com', 'password': '4_v8mee73RdRNrH'},
    {'email': 'xiajibaluanxiede@163.com', 'password': '-K42!FycASxT3mS'}
]

for user in users:
    # 创建浏览器对象
    browser = webdriver.Chrome(options=option,executable_path=chromedriver)

    # 将webdriver属性置为undefined
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                            {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})

    # 窗口最大化
    browser.maximize_window()

    # 访问网址 https://xhcy.us/
    start_time = time.time()  # 记录开始运行时间
    browser.get("https://xhcy.moe/account/lottery")

    # 显示等待，等待关闭按钮出现
    close_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.poi-dialog__footer__btn")))

    # 点击关闭按钮
    close_button.click()

    # 显示等待，等待登录按钮出现
    # login_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "inn-sign__login-btn")))

    # 点击登录按钮
    # login_button.click()

    # 显示等待，等待邮箱输入框出现
    email_input = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "email")))

    # 输入邮箱
    email_input.send_keys(user['email'])

    # 显示等待，等待密码输入框出现
    password_input = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "pwd")))

    # 输入密码
    password_input.send_keys(user['password'])

    # 显示等待，等待登录按钮出现
    submit_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.poi-dialog__footer__btn_success")))

    # 点击登录按钮
    submit_button.click()

    # 显示等待，等待关闭按钮出现
    close_button = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.poi-dialog__footer__btn")))

    # 点击关闭按钮
    close_button.click()

    #点击签到按钮
    try:
        wait = WebDriverWait(browser, 10)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inn-nav__point-sign-daily a')))
        button.click()
        # 显示等待，等待关闭按钮出现
        close_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.poi-dialog__footer__btn")))
        # 点击关闭按钮
        close_button.click()
        print(f"{user['email']}签到成功")
    except:
        print(f"{user['email']}签到失败")
    time.sleep(10)
    try:
        # 定位要点击的元素
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.inn-account__lottery__item.poi-list__item h3.inn-account__lottery__item__title')))
        element.click()
        button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "poi-btn_success")))
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'inn-user-code__container')))
        time.sleep(5)
        button.click()
        close_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.poi-dialog__footer__btn.poi-dialog__footer__btn_default'))
        )
        time.sleep(2)  # 可选的等待时间
        close_button.click()
    except:
        print(f"{user['email']}芯币领取失败")
    xpath = '//div[@class="inn-account__lottery__item poi-list__item"]//h3[contains(text(), "【心念祈愿】用户组 [念*终身]")]'
    element = WebDriverWait(browser, 10).until(
             EC.element_to_be_clickable((By.XPATH, xpath))
         )
    element.click()
    for _ in range(5):
     try:
         # 等待按钮出现并点击
         button = WebDriverWait(browser, 5).until(
             EC.presence_of_element_located((By.CLASS_NAME, "poi-btn_success"))
         )
         element = WebDriverWait(browser, 10).until(
             EC.presence_of_element_located((By.CLASS_NAME, 'inn-user-code__container'))
         )
         time.sleep(2)  # 可选的等待时间

         button.click()

         # 等待对话框出现并定位
         dialog = WebDriverWait(browser, 10).until(
             EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.poi-dialog__container.with-overlay'))
         )

         # 点击关闭按钮
         close_button = dialog.find_element(By.CSS_SELECTOR, 'button.poi-dialog__footer__btn')
         close_button.click()

     except Exception as e:
         print("出现异常:", e)


    endtime = time.time()  # 记录结束运行时间
    print(f"{user['email']}代码执行时间为：{endtime - start_time}秒")
    # 关闭浏览器
    browser.quit()
