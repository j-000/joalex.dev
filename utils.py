import smtplib
from email.message import EmailMessage
import os


def notifyme(subject, text):
    session = smtplib.SMTP('smtp.gmail.com', 587)        
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(os.getenv('MAIL_USERNAME'), os.getenv('MAIL_PASSWORD'))

    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = subject
    msg['From'] = os.getenv('MAIL_DEFAULT_SENDER')
    msg['To'] = os.getenv('TO_EMAIL')

    session.sendmail(from_addr=os.getenv('MAIL_DEFAULT_SENDER'), to_addrs=[os.getenv('TO_EMAIL')], msg=msg.as_string())
    session.quit()
