# Copyright (c) 2015-2018 Anish Athalye. Released under GPLv3.

import os

import numpy as np
import scipy.misc

import cv2

import stylize

import math
from argparse import ArgumentParser

from PIL import Image
from flask import Flask, request, render_template
import base64, datetime

app = Flask(__name__)

def NdarrayToBase64(img):
    result, img_data = cv2.imencode('.png', img)
    img_base64 = base64.b64encode(img_data).decode("UTF-8")
    return img_base64

def Base64ToNdarry(img64):
    img_data = base64.b64decode(img64.split(',')[1])
    img_np = np.fromstring(img_data, np.uint8)
    src = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)
    return src

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/picass', methods=['POST'])
def sample():
    content_base64 = request.form['image']
    content = Base64ToNdarry(content_base64)

    dt = datetime.datetime.today()
    dt_formatted = dt.strftime("%Y%m%d%H%M%S")
    extension = '.png'
    capture_img_name = os.path.join(app.config['./images'], 'cap_' + dt_formatted + extension)
    generate_img_name = os.path.join(app.config['./output'], 'gen_' + dt_formatted + extension)

    cv2.imwrite(capture_img_name, content)

    content_g = cv2.cvtColor(content, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(generate_img_name, content_g)

    return render_template('index.html', generate_img = generate_img_name, capture_img = capture_img_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
