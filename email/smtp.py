# 
# ! SMTP : Simple Mail Transfer Protocol
# * Using a process called "store and forward", SMTP moves your email on and across networks.
# * It works closely with something called the Mail Transfer Agent (MTA) to send your comunication to the right computer and email inbox. SMTP spells out and directs how your email moves from your computer's MTA to an MTA on another computer, and even several computers. Using that "store and forward" feature mentioned before, the message can move in steps from your computer to its destination.
# * SMTP is able to transfer only text. Fortunately, Multipurpose Internet Mail Extensions (MIME) were created to lend a hand, encodes all non-text content into plain text. In that transformed format, SMTP is coaxed into transfering the data.

# * Python provides smtplib module, wich defines an SMTP client session object that can be used to send mail to any internet machine with an SMT"P or ESMTP listener daemon.


# ! email = smtplib.SMTP( [host [,port [,local_hostname]]] )

# * host - This is the host running your SMTP server. You can specify IP address of the host or a domain name like tutorialspoint.com.
# * port - If you are providing host argument, then you need to specify a port, where SMTP server is listening. Usually this port would be 25.
# * local_hostname - if your SMTP server is running on your local machine. the you can specify just localhost as of this option.

import smtplib

sender = 'dimitritkach@gmail.com'
password = '' # todo inserisci la password della mail dalla quale invii e attiva per quel account accesso app meno sicure per inviare le mail da qui
receiver = 'dimatkach123454321@gmail.com'

subject = 'SMTP e-mail test'
text_message = 'This is a test e-mail message.'

message = f'''From: <{sender}>
To: <{receiver}>
Subject: {subject}

{text_message}
'''

try:
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465) # SSL "Secure Sockets Layer", a standard tecnology that ensures the security of an Internet connection and protects sensitive data exchanged between two systems by prevebting cybercriminals from reading and modifying the information transferred, wich may include personal data.
    smtpObj.login(sender, password)
    smtpObj.sendmail(sender, receiver, message)
    print(f'''
    Successfully sent mail
    From: {sender}
    To: {receiver}
    Subject: {subject} 
    ''')
except:
    print(f'Error with sending mail')

# ! MIME 
# * In most casses, you need to add some formatting, links, or images to your email notifications. We can simply put all of these with the HTML content. For this purpose, Python has an email package.
# * MIME is able to combine HTML and plain text. In python, it is handled by the email.mime module.
# * It is better to write a text version and an HTML version separately, and then merge them with the MIMEMultipart("alternative") istance. This means that such a message has two rendering options accordingly. In case an HTML is not rendered successfully for some reason, a text version will still be available.

import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = 'dimitritkach@gmail.com'
receiver_email = 'dimatkach123454321@gmail.com'
password = input('Type your password and press enter: ')

message = MIMEMultipart('alternative')
message['Subject'] = 'multipart test'
message['From'] = sender_email
message['To'] = receiver_email

text = '''
Hi, 
How are you?
'''
html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>email test</title>
</head>
<body>
    <p>
        Hi<br>
        How are you?<br>
        <a href="www.google.com">google</a>
    </p>
</body>
</html>
'''

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Add HTML/plain-text parts to MIMEMultipart message, the email client try to render the last part first 
message.attach(part1)
message.attach(part2) # invia questa parte in quanto last per prima e se qualcosa va storto invia la parte prima di last e cosi via in base agli attach()

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    try:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print(f'''
                Successfully sent mail
                From: {message['From']}
                To: {message['To']}
                Subject: {message['Subject']} 
            ''')
    except:
        print(f'Error with sending mail')