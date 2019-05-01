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

app = Flask(__name__)

@app.route('/picass/<content_name>')
def sample(content_name):
    content = cv2.imread('./images/' + content_name)
    content_g = cv2.cvtColor(content, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./output/' + content_name, content_g)
    return 'Success!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
