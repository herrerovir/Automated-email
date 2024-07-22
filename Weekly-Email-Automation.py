#Email Automation by Virginia Herrero

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime
import os
import csv

#Sender email credentials
my_email = input("Enter your email: ")
my_password = input("Enter your password: ")

#SMTP server info
gmail_server = "smtp.gmail.com"
gmail_port = 587

#Email content
msg = MIMEMultipart()
week_number = datetime.date.today().isocalendar()[1]
msg["Subject"] = f"Project Alpha: Report Email Week {week_number}"
message = f"""Hello Team, \n
Please find here the weekly report of the Alpha project for week {week_number}.\n
You will find the report attached to this email. In it you will find a detailed account of the activities carried out during this week and their results: notable achievements and areas for improvement. You will also find the list of tasks for the following week and the objectives to be achieved.\n
Please take a moment to read it and let me know if you have any questions or comments.\n
Thank you very much.
Best regards,\n
Your name
"""
msg.attach(MIMEText(message, "plain"))

#Attach file(s) to email
file = r"C:/Users/Reports/Weekly-report.pdf" #Change this path to the correct path where you have have the file you want to attach

with open(file, "rb") as f:
    attachment = MIMEApplication(f.read(), name = os.path.basename(file))
    attachment.add_header("Content-Disposition", "Attachment", filename = os.path.basename(file))
    msg.attach(attachment)

#Connect to the server, login and send email
try:
    server = smtplib.SMTP(gmail_server, gmail_port)
    server.ehlo() #client-server connection
    server.starttls() #encryption
    server.login(my_email, my_password) #login with sender credentials
    with open("weekly_report_contacts.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for email in reader:        
            server.sendmail(my_email, email, msg = msg.as_string()) #send emails to all the recipients in the csv file
    server.quit()
    print("Email sent sucessfully")

except Exception as e:
    print("Failed to send email. Error:", e)

