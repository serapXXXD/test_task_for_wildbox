FROM python:3.12

RUN mkdir /code

WORKDIR /code

COPY . .

RUN pip install -r ./requirements.txt

CMD ["celery", "-A", "checker", "beat", "-l", "INFO", "--scheduler", "django_celery_beat.schedulers:DatabaseScheduler"]