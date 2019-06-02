FROM nvcr.io/nvidia/tensorflow:19.04-py3
#FROM tensorflow/tensorflow:1.3.0-devel-py3
#FROM python:3.6.8-stretch

WORKDIR /app

#RUN echo  nameserver 192.30.0.2 >> /etc/resolv.conf

COPY ./requirements.txt /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN apt-get update

RUN apt-get install -y libsm6 libxext6 libxrender-dev libqt4-test


#RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64/

CMD ["python3", "app.py"]
