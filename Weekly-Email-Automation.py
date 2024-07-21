#Email Automation by Virginia Herrero

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#Sender email credentials
my_email = input("Enter your email: ")
my_password = input("Enter your password: ")

#Recipient email
to_email = "recipient-test@gmail.com"

#SMTP server info
gmail_server = "smtp.gmail.com"
gmail_port = 587

#Email content
msg = MIMEMultipart()
msg["From"] = my_email
msg["To"] = to_email
msg["Subject"] = "Automated Email Test"
text_message = "Hello this is a test"
msg.attach(MIMEText(text_message, "plain"))

#Connect to the server, login and send email
try:
    server = smtplib.SMTP(gmail_server, gmail_port)
    server.ehlo() #client-server connection
    server.starttls() #encryption
    server.login(my_email, my_password) #login with sender credentials
    server.sendmail(my_email, to_email, msg.as_string()) #send email
    server.quit()
    print("Email sent sucessfully")

except Exception as e:
    print("Failed to send email. Error:", e)

