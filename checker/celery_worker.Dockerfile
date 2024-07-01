FROM python:3.12

RUN mkdir /code

WORKDIR /code

COPY . .

RUN pip install -r ./requirements.txt

CMD ["celery", "-A", "checker", "worker", "-l", "INFO"]