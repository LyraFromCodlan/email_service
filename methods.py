from email.message import EmailMessage
from typing import Dict
import smtplib, ssl, appConfigParser as conf
from pydantic import BaseModel

SERVERTYPE = conf.SERVER
PORT = conf.SERVER_PORT
SENDER = conf.SENDER_EMAIL
PASSWORD = conf.PASSWORD

class RequestDto(BaseModel):
    reciever : str
    subject : str
    body : str

class RequestDtoList(BaseModel):
    recievers : Dict[str,str]
    subject : str
    body : str
    

def sendMail(request : RequestDto):
    try:
        email = EmailMessage()
        email['From'] = SENDER
        email['To'] = request.reciever
        email["Subject"] = request.subject
        email.set_content(request.body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(SERVERTYPE, PORT, context= context) as server:
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, request.reciever, email.as_string())
        return True
    except Exception as e:
        print(e)
        return False
    
def sendEmails(request: RequestDtoList):
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SERVERTYPE, PORT, context= context) as server:
            server.login(SENDER, PASSWORD)
            for recieverData, recieverEmail in request.recievers.items():
                email = EmailMessage()
                email['From'] = SENDER
                email['To'] = recieverEmail
                email["Subject"] = request.subject
                email.set_content(request.body+recieverData)
                server.sendmail(SENDER, recieverEmail, email.as_string())
        return True
    except Exception as e:
        print(e)
        return False