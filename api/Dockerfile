FROM python:3.7-alpine

MAINTAINER Willian Frantz willianluigii@gmail.com

ADD . /api

RUN pip install -r /api/requirements.txt

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:8000", "api.src.main:app"]