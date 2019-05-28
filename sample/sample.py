# Copyright (c) 2015-2018 Anish Athalye. Released under GPLv3.

import os

import numpy as np
import scipy.misc

import cv2

import stylize

import math
from argparse import ArgumentParser

from PIL import Image
from flask import Flask, Response, request, stream_with_context
import base64, requests

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

@app.route('/picass', methods=['POST'])
def sample():
    content_base64 = request.form['image']
    print(content_base64)
    content = Base64ToNdarry(content_base64)
    content_g = cv2.cvtColor(content, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('./output/' + content_name, content_g)
    #with open(SAVE_DIR + content_name, "rb") as f:
    #    rimg = f.read()
    #rimg64 = base64.b64encode(rimg).decode("UTF-8")
    return NdarrayToBase64(content_g)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
