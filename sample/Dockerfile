#FROM nvcr.io/nvidia/tensorflow:19.04-py3
#FROM tensorflow/tensorflow:1.3.0-devel-py3
FROM python:3.6.8-stretch

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "sample.py"]
