from email.mime.text import MIMEText
import smtplib
import sys

def send_email_(to_email, from_email, subject, message ,password):
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, password)
    gmail.send_message(msg)

def send_json(data):
    '''
    data is a dictionary
    '''
    try:
        from_email = input("From Email: ")
        password = input("Password: ")
        to_email = input("To Email: ")
        massage = ""
        subject = "Email # 1"
        for email_ , height_ in zip(data['email'], data['height'] ):
            massage = massage + email_ + ': ' + height_  + '<br>'
        send_email_(to_email, from_email, subject, massage ,password)
        print(massage)
    except:
        print("the email username/password is not correct")






