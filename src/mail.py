import smtplib, traceback
from email.mime.text import MIMEText
from email.header import Header

from config.mail_config import mail_config
from log.logger import logger as log

def send_mail(subject, content, receiver):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(mail_config["user"], 'utf-8')
    message['To'] = Header(mail_config["to"], 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_config["host"], 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_config["user"], mail_config["passwd"])
        smtpObj.sendmail(mail_config["user"], receiver, message.as_string())
        log.info("mail sent success.")
    except smtplib.SMTPException as e:
        log.error("mail sent failed")
        log.error(str(e))
        log.error(traceback.format_exc())