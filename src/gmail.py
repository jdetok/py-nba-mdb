import os
import glob
import smtplib
from datetime import datetime
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_summary():
    load_dotenv()
    sender = os.environ['GMAIL_SNDR']
    receiver = os.environ['GMAIL_RCVR']
    server = os.environ['GMAIL_URL']
    port = os.environ['GMAIL_PORT']
    password = os.environ['GMAIL_PASS']
    
    # build email
    msg = MIMEMultipart()
    msg['From'] = receiver
    msg['To'] = sender
    msg['Subject'] = f'NBA ETL script complete - {datetime.today().strftime("%m/%d/%Y %H:%M")}'
    body = MIMEText(f'Insert summaries attached')
    msg.attach(body)
    
    # get the most recent log file and attach
    with open(get_recent_log('logs'), 'rb') as f:
        msg.attach(MIMEApplication(f.read(), name='nba_etl_summary.txt'))
        
    # send the email using gmail
    with smtplib.SMTP_SSL(server, port) as gmail:
        gmail.login(sender, password)
        gmail.sendmail(sender, receiver, msg.as_string())

# find recent log (not really necessary anymore with running in docker)
def get_recent_log(dir):
    ls = glob.glob(os.path.join(dir, '*'))
    if not ls:
        return None
    return max(ls, key=os.path.getmtime)