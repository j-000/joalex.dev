FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV ENV='production'

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", \
    "-w", "4", "--log-level=debug", \
    "--access-logfile", "./shared_data/access.gunicorn.log", \
    "--error-logfile", "./shared_data/error.gunicorn.log", \
    "app"]