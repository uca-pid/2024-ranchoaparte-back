from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from typing import List


conf = ConnectionConfig(
    MAIL_USERNAME ="healthybitepid@gmail.com",
    MAIL_PASSWORD = "DelfiJoseTpPid2024",
    MAIL_FROM = "healthybitepid@gmail.com",
    MAIL_PORT = 465,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True)

async def send_email (subject: str, reci: list,  message: str):
    message= MessageSchema(
        subject=subject,
        recipients =reci,
        body= message,
        subtype ='html',
    )
    fm = FastMail(conf)
    await fm.send_message(message)