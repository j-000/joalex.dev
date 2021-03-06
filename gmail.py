import smtplib
from email.message import EmailMessage


def notifyme(subject, text):
    session = smtplib.SMTP('smtp.gmail.com', 587)        
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login('joaoalexsilva1@gmail.com', 'Jasoliv1993#')

    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = subject
    msg['From'] = "joaoalexsilva1@gmail.com"
    msg['To'] = "jjasilva85@gmail.com"

    session.sendmail(from_addr='joaoalexsilva1@gmail.com', to_addrs=['jjasilva85@gmail.com'], msg=msg.as_string())
    session.quit()

