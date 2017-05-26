#-*-coding:utf-8-*-

#==========================================
# 导入smtplib和MIMEText
#==========================================
from email.mime.text import MIMEText
import smtplib
#==========================================
# 要发给谁，这里发给2个人
#==========================================
mailto_list=["604135528@qq.com","964219733@qq.com"]
#qjj = ["964219733@qq.com"]
#==========================================
# 设置服务器，用户名、口令以及邮箱的后缀
#==========================================
mail_host="smtp.qq.com"
mail_user="604135528"
mail_pass="bllvwnnzywfvbfid"#qq要求授权码，密码不行，你要在手机发短信具体的上qq邮箱网站上看
mail_postfix="qq.com"
#==========================================
# 发送邮件
#==========================================
def send_mail(to_list,sub,content):
  '''''
  to_list:发给谁
  sub:主题
  content:内容
  send_mail("xxx@xxxx.com","主题","内容")
  '''
  me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
  msg = MIMEText(content)
  msg['Subject'] = sub
  msg['From'] = me
  msg['To'] = ";".join(to_list)
  try:
    s = smtplib.SMTP_SSL(mail_host, 465)
    s.set_debuglevel(1)
    s.login(mail_user,mail_pass)
    s.sendmail(me, to_list, msg.as_string())
    s.close()
    return True
  except Exception:
    print("error")
    return False

if __name__ == '__main__':
    content = ""
    with open("F:/workspace/python/seCrawler-master/seCrawler/spiders/search_result.txt","r") as read:
        con =read.readlines()
        for c in con:
            content = content +"\n"+con
    print(content)


  # if send_mail(mailto_list,"content from crawl ",""):
  #   print("发送成功")
  # else:
  #   print("发送失败")