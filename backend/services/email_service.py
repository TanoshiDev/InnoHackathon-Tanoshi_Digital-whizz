import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import HTTPException

from config import (
    SMTP_SERVER,
    SMTP_PORT,
    SMTP_USERNAME,
    SMTP_PASSWORD,
    EMAIL_FROM,
    EMAIL_TO,
)


def send_feedback_email(user_login: str, title: str, description: str):
    subject = f"Feedback from {user_login}: {title}"
    body = f"User: {user_login}\n\nTitle: {title}\n\nDescription:\n{description}"

    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        if SMTP_PORT == 465:
            server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
        else:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication failed: {e}")
        raise HTTPException(
            status_code=500, detail="Authentication failed while sending email."
        )
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise HTTPException(
            status_code=500, detail="An error occurred while sending email."
        )
