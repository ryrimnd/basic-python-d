#Importing Packages
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

alamatemailnya = []
listalamatemail = []
file = open("receiver_list.txt", "r")
for i in file:
    alamatemailnya.append(i)
for x in alamatemailnya:
    listkatahapus = x.replace("\n","")
    listalamatemail.append(listkatahapus)

#Sender, Reciever, Body of Email
sender = 'ryhnrzkykbr@gmail.com'
receivers = listalamatemail
body_of_email = 'Ini emailnya masuk ga?'

#Creating the Message, Subject line, From and To
msg = MIMEText(body_of_email, 'html')
msg['Subject'] = 'Masuk ga?'
msg['From'] = sender
msg['To'] = ','.join(receivers)

#Connecting to Gmail SMTP Server
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = sender, password = 'rrakbar30')
s.sendmail(sender, receivers, msg.as_string())
s.quit()

'''
#Importing Packages
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Sender, Reciever, Body of Email
sender = 'your_email@email.com'
receivers = ['recipient1@recipient.com', 'recipient2@recipient.com']
body_of_email = 'Text to be displayed in the email'

#Creating the Message, Subject line, From and To
msg = MIMEText(body_of_email, 'html')
msg['Subject'] = 'Subject line goes here'
msg['From'] = sender
msg['To'] = ','.join(receivers)

#Connecting to Gmail SMTP Server
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = 'your_username', password = 'your_password')
s.sendmail(sender, receivers, msg.as_string())
s.quit()
'''