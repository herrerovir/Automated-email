#Email Automation by Virginia Herrero

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime, time
import os
import csv
import schedule

#Sender email credentials
my_email = input("Enter your email: ")
my_password = input("Enter your password: ")

#SMTP server info
gmail_server = "smtp.gmail.com"
gmail_port = 587

week_number = datetime.date.today().isocalendar()[1]

#Email body content
body = f"""Hello NAME, \n
Please find here the weekly report of the Alpha project for week {week_number}.\n
You will find the report attached to this email. In it you will find a detailed account of the activities carried out during this week and their results: notable achievements and areas for improvement. You will also find the list of tasks for the following week and the objectives to be achieved.\n
Please take a moment to read it and let me know if you have any questions or comments.\n
Thank you very much.
Best regards,\n
Your name
"""

#Function to send the email
def send_email():
    try:
        #Connect to the server
        server = smtplib.SMTP(gmail_server, gmail_port)
        server.ehlo() #client-server connection
        server.starttls() #encryption
        server.login(my_email, my_password) #login with sender credentials

        #Get email recipient from csv file
        with open("weekly_report_contacts.csv") as file:
            reader = csv.reader(file)
            next(reader)
            for name, email in reader:
                #Create multipart email
                msg = MIMEMultipart()
                msg["From"] = my_email
                msg["To"] = email
                msg["Subject"] = f"Project Alpha: Report Email Week {week_number}"
                message = body.replace("NAME", name)
                msg.attach(MIMEText(message, "plain")) #Attach text part to email

                #Attach file(s) to email
                file = r"C:/Users/Reports/Weekly-report.pdf"
                with open(file, "rb") as f:
                    attachment = MIMEApplication(f.read(), name = os.path.basename(file))
                    attachment.add_header("Content-Disposition", "Attachment", filename = os.path.basename(file))
                    msg.attach(attachment)

                #Send email
                server.sendmail(my_email, email, msg = msg.as_string()) #send emails to all the recipients in the csv file

        print("Email sent sucessfully")
    except Exception as e:
        print("Failed to send email. Error:", e)
        
        server.quit()

#Schedule script to run weekly
schedule.every().monday.at("12:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
    send_email()