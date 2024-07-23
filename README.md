# Weekly Email Automation
![GitHub top language](https://img.shields.io/github/languages/top/herrerovir/Automated-email) ![GitHub License](https://img.shields.io/github/license/herrerovir/automated-email)

Email automation is a powerful tool that allows you to send emails to the right people at the scheduled time, without having to do the work over and over again. 
Thus, email automation takes repetitive tasks off your to-do list and leaves you time to do other valuable tasks.

This super useful and convenient program written in Python allows you to send weekly emails to different recipients obtained from a csv file with a file attachment. 

The program starts asking the user to introduce the email and password from their Gmail account. 
Next, it will retrieve the recipients from the csv file named "weekly_report_contacts.csv" and send an email to each of them at a scheduled time every Monday. 
The email contains a body message, personalized with the name of each reicipient, and a "Weekly-report" pdf file as an attachment. 

The code consists of two files: Weekly-email-automation.py and weekly-report-contacts.csv. Please, have in mind that both files must be stored in the same directory, otherwise the program will not work. 

## Dependencies:

Python 3

Libraries used: smtplib, from email.mime.multipart: MIMEMultipart, from email.mime.text: MIMEText, from email.mime.application: MIMEApplication, datetime, time, os, csv, schedule


## How to run the script:

* Clone or download the repository to your local machine
* Create an app password for your Gmail account in the security tab in your Google account
* Add the names and email addresses of your recipients in the "weekly-report-contacts.csv" file
* Customise the body of the email to your liking
* Customise the subject of your email
* Set the correct path of the file you want to attach to the email
* Set the day and hour you want to send your email on a weekly basis 
* Run the Weekly-email-automation.py file in a Python environment
* Get ready to send weekly emails with a pdf attachment without any effort!

## License:

This project is licensed under the MIT License. See the [LICENSE](LICENSE)  file for details
