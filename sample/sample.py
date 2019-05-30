# Copyright (c) 2015-2018 Anish Athalye. Released under GPLv3.

import os

import numpy as np
import scipy.misc

import cv2

import stylize

import math
from argparse import ArgumentParser

from PIL import Image
from flask import Flask, request, render_template, send_file, url_for, jsonify
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

@app.route('/images/<path:path>')
def get_image(path):
    return send_file('images/' + path)

@app.route('/picass', methods=['GET', 'POST'])
def sample():
    if request.method == 'POST':
        content_base64 = request.form['image']
        content = Base64ToNdarry(content_base64)

        dt = datetime.datetime.today()
        dt_formatted = dt.strftime("%Y%m%d%H%M%S")
        extension = '.png'
        capture_img_name = os.path.join('/images/input', 'cap_' + dt_formatted + extension)
        generate_img_name = os.path.join('/images/output', 'gen_' + dt_formatted + extension)

        cv2.imwrite('/app/' + capture_img_name, content)

        content_g = cv2.cvtColor(content, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('/app/' + generate_img_name, content_g)

        res = {
            'org_url' : capture_img_name,
            'gen_url'  : generate_img_name
        }    

        return jsonify(res)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
