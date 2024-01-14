import smtplib, ssl
from email.message import EmailMessage

def send_notification(text):

    sender_email = "kevin.solartent@gmail.com"  # Enter your address
    receiver_email = "shiningsword@gmail.com"  # Enter receiver address
    password = "xoslletnbsqgbqtb"

    msg = EmailMessage()

    msg.set_content(text)

    msg['Subject'] = 'Property found'
    msg['From'] = sender_email
    msg['To'] = receiver_email


    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login(sender_email, password)
    
    # sending the mail
    s.sendmail(sender_email, receiver_email, msg.as_bytes())
    
    # terminating the session
    s.quit()