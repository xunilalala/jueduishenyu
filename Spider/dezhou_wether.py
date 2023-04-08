import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import requests
import datetime
import calendar

# 获取当前日期和本月最后一天的日期
today = datetime.date.today()
last_day_of_month = today.replace(day=calendar.monthrange(today.year, today.month)[1])

# 计算距离月底还剩多少天
days_remaining = (last_day_of_month - today).days

# 将结果保存到变量day中
day = days_remaining

# 设置收件人列表
to_list = ['3120294679@qq.com', '18264410349@163.com','226302770@qq.com','2505668044@qq.com','3220653844@qq.com']

# 邮件正文中的话
message = "Thank you for subscribing to the \"Weather Forecast Monthly/2 $\" service. There are " + str(day) + " days left until the end of the service. In order to ensure your experience, please renew in a timely manner."

# 获取图片
response = requests.get("https://wttr.in/dezhou.png")

smtp_server = "smtp.qq.com"
smtp_port = 25
smtp_username = "1592585947@qq.com"
smtp_password = "skuioorvpiumheif"

for to in to_list:
    # 创建MIMEMultipart对象
    msg = MIMEMultipart()

    # 设置邮件标题
    msg['Subject'] = "Weather Forecast DeZhou"

    # 设置发件人
    msg['From'] = smtp_username

    # 设置收件人
    msg['To'] = to

    # 创建MIMEText对象，添加正文
    text = MIMEText(message + '<br><img src="cid:image1">', 'html')
    msg.attach(text)

    # 创建MIMEImage对象，添加图片
    image = MIMEImage(response.content)
    image.add_header('Content-ID', '<image1>')
    msg.attach(image)

    # 发送邮件
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, to, msg.as_string())
    server.quit()
    print(f"Email sent to {to} successfully!")
