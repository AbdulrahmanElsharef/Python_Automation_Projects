import schedule
import time
import smtplib
from email.mime.text import MIMEText


def send_mail():
    ''' function creat smtp session for send mail
    args:send_mail,token_mail,reciv_mail,message
    return:sendmail(send_mail, reciv_mail, message)'''
    # creates SMTP session
    sms = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    sms.starttls()
    sender = 'nour70331@gmail.com' 
    receiver = 'abdoelsharef1@gmail.com'
    msg = MIMEText(
        f"white friday {receiver} you have sale 50% offer for iphone accseorice click here to take sale ".title())
    msg['Subject'] = 'white friday'.upper()
    msg['From'] = sender
    msg['To'] = 'customer'.upper()
    token_mail = "wxgbbvaengzrypoj"   # mail_pass_token
    # Authentication
    sms.login(sender, token_mail)
    # message to be sent
    # sending the mail
    sms.sendmail(sender, receiver, msg.as_string())
    # terminating the session
    sms.quit()
    print(f"send mail to {receiver} is done ...".title())


schedule.every(10).seconds.do(send_mail)
while True:
    schedule.run_pending()
    time.sleep(1)  # wait


# (بدون موضوع)
# البريد الوارد

# nour70331@gmail.com
# 12:36 م ‎(قبل 0 دقيقة)‎


# ترجمة الرسالة
# اخفاء خيارات الترجمة من الإنجليزية
# White Friday  [44M [33Mabdoelsharef1@Gmail.Com [0M You Have Sale 50% Offer For Iphone Accseorice Click Here To Take Sale


# 1 من 150
# WHITE FRIDAY‏‏
# البريد الوارد

# nour70331@gmail.com
# 1:00 م ‎(قبل 0 دقيقة)‎
# CUSTOMER

# White Friday ['Abdoelsharef1@Gmail.Com'] You Have Sale 50% Offer For Iphone Accseorice Click Here To Take Sale
