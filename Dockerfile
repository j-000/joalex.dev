FROM python:3.6.6-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV ENV='development'
ENV MAIL_USERNAME=''
ENV MAIL_PASSWORD=''
ENV MAIL_DEFAULT_SENDER=''
ENV TO_EMAIL=''
ENV S3_KEY = ''
ENV S3_SECRET_KEY = ''

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]