FROM nvcr.io/nvidia/tensorflow:19.04-py3

WORKDIR /app

#RUN echo  nameserver 192.30.0.2 >> /etc/resolv.conf

COPY ./requirements.txt /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN apt-get update

RUN apt-get install -y libsm6 libxext6 libxrender-dev

CMD ["python", "app.py"]
