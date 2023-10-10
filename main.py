# the task for this project was automate the process of sending daily reports via email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule

# write your full email address
fromaddr = 'enter your email'

# list of the recipient`s
lst = ["firstemail@gmail.com", "secondemail@gmail.com", 'thirdemail@gmail.com', '...']


def autosending():
    for dest in lst:

        # connection to gmail
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # tls security
        s.starttls()

        # generate 16digit app password for this step in your google settings
        s.login(fromaddr, 'your email password')
        msg = MIMEMultipart()

        # text of the message
        body = 'Here is your daily report'

        # attaching text from body to your message
        msg.attach(MIMEText(body, "plain"))
        filename = 'full file name'

        # full path to the file
        attachment = open('report file path', 'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attaching file to your message
        msg.attach(p)

        # constructing the message
        msg['From'] = fromaddr
        msg['To'] = dest
        msg['Subject'] = 'Daily report'
        text = msg.as_string()

        # sending the message
        s.sendmail(fromaddr, dest, text)

        # ending current process
        s.quit()

# scheduling the auto sending
schedule.every().day.at('12:00').do(autosending)
while True:
    schedule.run_pending()
