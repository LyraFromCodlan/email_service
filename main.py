from email.message import EmailMessage
from fastapi import FastAPI
from pydantic import BaseModel
import smtplib, ssl, appConfigParser as conf

class RequestDto(BaseModel):
    reciever : str
    subject : str
    body : str

    

def sendMail(request : RequestDto):
    try:
        smtp_server = conf.SERVER
        port = conf.SERVER_PORT
        sender_email = conf.SENDER_EMAIL
        password = conf.PASSWORD
        reciever_email = request.reciever
        

        email = EmailMessage()
        email['From'] = sender_email
        email['To'] = request.reciever
        email["Subject"] = request.subject
        email.set_content(request.body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context= context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, email.as_string())
        return True
    except Exception as e:
        print(e)
        return False
    



app = FastAPI()

@app.post("/EmailService/api/email")
async def emailService(request: RequestDto):
    return sendMail(request=request)