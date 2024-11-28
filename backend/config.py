import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY не установлен в переменных окружения")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1337

SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.mail.ru")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "465"))
SMTP_USERNAME = os.environ.get("SMTP_USERNAME", "help@whizz.guru")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
EMAIL_FROM = os.environ.get("EMAIL_FROM", SMTP_USERNAME)
EMAIL_TO = os.environ.get("EMAIL_TO", "help@whizz.guru")
