import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 从 GitHub Secrets 中读取配置，这是安全的做法
mail_username = os.environ["MAIL_USERNAME"]
mail_password = os.environ["MAIL_PASSWORD"]
to_email = os.environ["TO_EMAIL_ADDRESS"]

# 构造邮件内容
msg = MIMEText('这是一封通过 GitHub Actions 自动发送的测试邮件。', 'plain', 'utf-8')
msg['Subject'] = Header('来自 GitHub Actions 的问候', 'utf-8')
msg['From'] = mail_username
msg['To'] = to_email

# 连接 163 邮箱的 SMTP 服务器并发送（如果你用其他邮箱，需修改服务器地址）
with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
    server.login(mail_username, mail_password)
    server.sendmail(mail_username, [to_email], msg.as_string())

print("邮件发送成功！")
