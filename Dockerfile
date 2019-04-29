FROM nvcr.io/nvidia/tensorflow:19.04-py3

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

CMD ["python", "neural_style.py"]
