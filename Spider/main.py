import concurrent.futures
import os

def run_script(script_name):
    os.system("python " + script_name)

if __name__ == "__main__":
    # 设置需要同时启动的py文件列表
    script_list = ["ACGAF.py", "jueduishenyu.py", "shendai.py","yuzhai.py","xingmeng.py","xinhuan.py",]

    # 创建线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(script_list)) as executor:
        # 提交每个脚本的任务
        futures = [executor.submit(run_script, script_name) for script_name in script_list]

        # 等待所有任务完成
        concurrent.futures.wait
