from fastapi import FastAPI
from methods import *

emailService = FastAPI()

@emailService.post("/EmailService/api/email")
async def sendSingleEmail(request: RequestDto):
    return sendMail(request=request)

@emailService.post("/EmailService/api/emails")
async def sendMultipleEmails(request: RequestDtoList):
    return sendEmails(request)