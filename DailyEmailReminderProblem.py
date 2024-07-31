import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as dt

def send_email(subject, body, to_email):
    # Email server settings
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = 'your_email@gmail.com'
    password = 'your_password'

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to the server and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

if __name__ == '__main__':
    # Email details
    subject = 'Daily Reminder'
    body = f'This is your daily reminder. The current date and time is {dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.'
    to_email = 'recipient_email@example.com'
    
    send_email(subject, body, to_email)
    print("Email sent successfully.")
