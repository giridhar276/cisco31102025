



import smtplib, ssl
from email.message import EmailMessage

# --- Configure these ---
SMTP_HOST, SMTP_PORT = "smtp.gmail.com", 465  # SSL port
USER = "yourmailid"                       # full Gmail address
APP_PASSWORD = "yourpassword"          # 16-char App Password
TO = ["giridhar276@gmail.com"]                 # one or more recipients
SUBJECT = "Hello from Python"
BODY = "This is a test email sent using Python and Gmail SMTP."
# ------------------------

msg = EmailMessage()
msg["From"] = USER
msg["To"] = ", ".join(TO)
msg["Subject"] = SUBJECT
msg.set_content(BODY)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as s:
    s.login(USER, APP_PASSWORD)
    s.send_message(msg)

print("Email sent ✓")



#https://myaccount.google.com/security
#https://myaccount.google.com/apppasswords