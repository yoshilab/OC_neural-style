import os
import cv2
import json
import tempfile
# import subprocess

from flask import Flask, Response, request, stream_with_context
from src import Gan

CAMERA_PORT = -1
CASCADE_PATH = './src/haarcascades/haarcascade_frontalface_alt2.xml'

app = Flask(__name__)

#logger = Logger()

def draw(content, style, output):
    gan = Gan()
    output_img = gan.generate(content, style, output)
    return output

@app.route('/picasso/<content>')
def picasso(content):
    output = './output_images/picasso_' + content
    draw(content, '/app//style_images/picasso.jpg', output)
    return output

@app.route('/gogh/<content>')
def gogh(content):
    output = './output_images/gogh_' + content
    draw(content, '/app/style_images/gogh.png', output)
    return output

@app.route('/munch/<content>')
def munch(content):
    output = './output_images/munch_' + content
    draw(content, '/app/style_images/munch.jpg', output)
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
