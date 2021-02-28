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
body_of_email = 'Nayeon and Tzuyu'

#Creating the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'TWICE'
msg['From'] = sender
msg['To'] = ','.join(receivers)

#Adds a csv file as an attachment to the email 
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('C:/Users/RYHN/Desktop/598933.jpg', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="NayeonandTzuyu.jpg"')
msg.attach(part)

#Connecting to Gmail SMTP Server
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = sender, password = 'rrakbar30')
s.sendmail(sender, receivers, msg.as_string())
s.quit()