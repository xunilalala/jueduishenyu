import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import time as timer
from concurrent.futures import ThreadPoolExecutor
import os


def calculate_total_size(text):
    sizes = re.findall(r'(\d+(\.\d+)?)\s*([TGMK])】', text)
    total_size = 0
    for size, _, unit in sizes:
        size = float(size)
        if unit == 'T':
            total_size += size
        elif unit == 'G':
            total_size += size / 1024
        elif unit == 'M':
            total_size += size / (1024 * 1024)
        elif unit == 'K':
            total_size += size / (1024 * 1024 * 1024)
        else:
            total_size = 0
    return total_size


def scrape_page(page):
    # 伪装请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Cookie': cookie
    }

    url = f"http://www.acg088.com/page/{page}"
    print(f"当前正在捕获第{page}页")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    div_container = soup.select_one("#rizhuti_v2_module_lastpost_item-3")
    divs = div_container.find_all("div", class_="col-lg-5ths col-lg-3 col-md-4 col-6")

    page_data = []

    for div in divs:
        title = div.find("h2", class_="entry-title").text.strip()
        time_tag = div.find("span", class_="meta-date")
        time_str = time_tag.find("time")["datetime"]
        time = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S%z")

        formatted_time = time.strftime("%Y-%m-%d")
        # 提取二级网址
        entry_media = div.find("div", class_="entry-media")
        second_level_url = entry_media.find("a")["href"]
        # 访问二级网址
        second_response = requests.get(second_level_url, headers=headers)
        second_soup = BeautifulSoup(second_response.text, "html.parser")
        div_element = second_soup.find("div", class_="entry-content u-text-format u-clearfix")
        p_element = div_element.find("p")
        if p_element is not None:
            content = p_element.get_text().strip()
        else:
            content = ""
        if is_summary:
            page_data.append((title, content, formatted_time))
        else:
            # 提取三级网址和密码
            btn_group = second_soup.find("div", class_="btn-group btn-block mt-2")
            third_level_url = btn_group.find("a")["href"]
            password = btn_group.find("button", class_="go-copy")["data-clipboard-text"]

            # 访问三级网址并获取四级网址
            third_response = requests.get(third_level_url, headers=headers, allow_redirects=False)
            if third_response.status_code == 302:
                fourth_level_url = third_response.headers["Location"]
            else:
                fourth_level_url = ""

            page_data.append((title, content, formatted_time, second_level_url, third_level_url, password, fourth_level_url))

    return page_data


def scrape_acg088(is_summary, cookie):
    # 记录开始时间
    start_time = timer.time()

    start_page = 2
    end_page = 365  # 为了调试，将 end_page 设置为 3
    flag = 0

    if is_summary:
        file_name = "简略信息.txt"
    else:
        file_name = "完整信息.txt"

    with open(file_name, "w", encoding="utf-8") as file:
        with ThreadPoolExecutor(max_workers=16) as executor:
            futures = [executor.submit(scrape_page, page) for page in range(start_page, end_page + 1)]

            for future in futures:
                page_data = future.result()

                for data in page_data:
                    title, content, formatted_time, *extra_data = data

                    file.write("标题: " + title + "\n")
                    file.write("内容: " + content + "\n")
                    file.write("时间: " + formatted_time + "\n")

                    if not is_summary:
                        second_level_url, third_level_url, password, fourth_level_url = extra_data

                        file.write("二级网址: " + second_level_url + "\n")
                        file.write("三级网址: " + third_level_url + "\n")
                        file.write("密码: " + password + "\n")
                        file.write("四级网址: " + fourth_level_url + "\n")

                    file.write("\n")
                    flag += 1

    print()
    print(f"共收录{flag}条消息")

    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
    total_size = calculate_total_size(text)
    header_line = f"总大小为{total_size:.2f}TB\n"

    header_line = f"共收录{flag}条信息，总大小为{total_size:.2f}T\n"
    with open(file_name, 'r+', encoding='utf-8') as file:
        content = file.read()
        file.seek(0, 0)
        file.write(header_line + content)

    print(header_line)

    end_time = timer.time()
    run_time = end_time - start_time
    run_time_minutes = run_time / 60
    print("程序运行时间：{:.2f}分钟".format(run_time_minutes))


# 获取当前工作目录的路径
current_path = os.getcwd()

# 打印当前路径
print("当前路径:", current_path)

# 调用函数并传入参数
is_summary = True
cookie = 'wordpress_logged_in_baec826e068566e2c7fc540b85d003db=xuni256%7C1689770755%7CuzDSsiVsbyCjmSTWeHqQ0Dpli89rtbSqyZTGXB2aDk8%7Cbf8901065719bab77ac359536ef1ee64ea5cf907fcac9dde0dc1b74180c22dd7; ripro_notice_cookie=1'
is_summary = False
scrape_acg088(is_summary, cookie)
