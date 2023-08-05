import subprocess

# 要执行的 Bash 命令
bash_command = "node ./chrome/jd_plantBean.js"

# 使用 subprocess.run 执行命令
result = subprocess.run(bash_command, shell=True, text=True, capture_output=True)

# 打印命令的输出
print("Command output:", result.stdout)
