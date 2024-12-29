import smtplib
from email.mime.text import MIMEText
import pandas as pd
from time import sleep

# Email settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your_email@gmail.com'
SENDER_PASSWORD = 'your_password'

# Load email list from a CSV
email_data = pd.read_csv('email_list.csv')  # Columns: Name, Email, Company

# Function to send email
def send_email(to_email, subject, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Email content template
subject_template = "Exciting opportunity for {Name}"
body_template = """
Hi {Name},

I hope this email finds you well. I wanted to reach out regarding {Company} and discuss how we can collaborate.

Looking forward to hearing from you.

Best,
Your Name
"""

# Send emails
for index, row in email_data.iterrows():
    subject = subject_template.format(Name=row['Name'])
    body = body_template.format(Name=row['Name'], Company=row['Company'])
    send_email(row['Email'], subject, body)
    sleep(5)  # Pause to avoid spam detection
