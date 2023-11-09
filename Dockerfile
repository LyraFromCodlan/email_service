FROM python:3.10-slim

WORKDIR /usr/src/emailService

COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000

COPY ./ /usr/src/emailService/ 

CMD ["uvicorn", "main:emailService", "--host", "0.0.0.0", "--port", "8000"]