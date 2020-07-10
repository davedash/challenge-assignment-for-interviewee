FROM python:3.8-alpine

ADD requirements.txt /
ADD scores.yaml /
ADD challenge.py /

RUN pip install -r requirements.txt

RUN python challenge.py
