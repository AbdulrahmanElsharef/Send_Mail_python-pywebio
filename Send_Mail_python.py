from pywebio.input import *
from pywebio.output import *
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
    sender = input_group("my email".title(),[
    input('enter your email please '.title(), name='my_email'),
    input('enter your password or token please'.title(), name='my_pass' , type=PASSWORD)])
    # sender =input("enter your email please".title())  
    receiver = input("send  to email please".title())
    mail = input_group("email message".title(),[
    input('mail subject'.title(), name='subject'),
    textarea('mail message'.title(), rows=3, name='message')])
    
    msg = MIMEText(mail['message'])
    msg['Subject'] = mail['subject']
    msg['From'] = sender['my_email']
    msg['To'] = receiver
    # token_mail = sender['mypass']   # mail_pass_token
    # Authentication
    sms.login(sender['my_email'], sender['my_pass'])
    # message to be sent
    # sending the mail
    sms.sendmail(sender['my_email'], receiver, msg.as_string())
    # terminating the session
    sms.quit()
    put_text(f"send mail to {receiver} is done ...".title()).style('color: yellow; font-size: 45px')

if __name__=="__main__":
    send_mail()


# nour70331@gmail.com
# tczbejrhneaenmcj
# abdoelsharef1@gmail.com