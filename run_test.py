# user/bin/python3
# coding:utf-8


import unittest
import HTMLReport
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from email.mime.multipart import MIMEMultipart


# 查找测试报告目录，找到最新生成的测试报告文件
def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getatime(test_report + "\\" + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    stmpserver = 'smtp.qq.com'
    user = "975216162@qq.com"
    # 这里填邮箱的授权码
    password = "jizikjnmxtfibegf"
    subject = '自动化测试报告'

    # 构造MIMEMultipart对象做为根容器
    msgRoot = MIMEMultipart()
    text_msg = MIMEText(mail_body, 'html', 'utf-8')
    msgRoot.attach(text_msg)
    file_msg = MIMEText(mail_body, 'base64', 'utf-8')
    file_msg["Content-Type"] = 'application/octet-stream'

    # 设置附件头
    basename = os.path.basename(file_new)
    print(basename)
    file_msg["Content-Disposition"] = 'attachment; filename=''' + basename + ''
    msgRoot.attach(file_msg)

    # 设置根容器属性
    msgRoot['Subject'] = Header(subject, 'utf-8')
    msgRoot['From'] = '975216162@qq.com'
    msgRoot['To'] = 'chenyongyan1525@dingtalk.com'

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(stmpserver)
    smtp.login(user, password)
    smtp.sendmail(msgRoot['From'], msgRoot['To'], msgRoot.as_string())
    smtp.quit()
    print('测试报告附件邮件已发送！')


if __name__ == "__main__":
    test_dir = "E:\\AutoTest\\TestCase"
    test_report = "E:\\AutoTest\\TestReport"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = 'E:\\AutoTest\\TestReport\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = unittest.TextTestRunner(verbosity=2)
    runner = HTMLReport.HTMLTestRunner(stream=fp, title='用例测试报告', description='用例执行情况:')
    runner.run(discover)
    fp.close()
    new_report = new_report(test_report)
    send_mail(new_report)
