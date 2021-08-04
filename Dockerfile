FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV ENV='development'

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]