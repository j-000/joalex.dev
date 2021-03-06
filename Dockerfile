FROM python:3.6.6-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV ENV='production'
ENV MAIL_USERNAME=''
ENV MAIL_PASSWORD=''
ENV MAIL_DEFAULT_SENDER=''
ENV TO_EMAIL=''

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]