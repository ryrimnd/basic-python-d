import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = 'ryhnrzkykbr@gmail.com'
password = 'rrakbar30'
send_to_email = 'ryhnrzkykbr@gmail.com'
subject = 'Remember' # The subject line
message = 'Yang bisa pake s2'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

 # Attach the message to the MIMEMultipart object
msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string() # You now need to convert the MIMEMultipart object to a string to send
server.sendmail(email, send_to_email, text)
server.quit()