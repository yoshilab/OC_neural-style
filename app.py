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

def NdarrayToBase64(img):
    result, img_data = cv2.imencode('.png', img)
    img_base64 = base64.b64encode(img_data).decode("UTF-8")
    return img_base64

def Base64ToNdarry(url_base64):
    img_data = base64.urlsafe_b64decode(url_base64)
    img_np = np.fromstring(img_data, np.uint8)
    src = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)
    return src

def draw(content, style):
    gan = Gan()
    output_img = gan.generate(content, style, output)
    return output_img

@app.route('/picasso/<content>')
def picasso(content):
    content = Base64ToNdarry(content_base64)
    #output = './output_images/picasso_' + content
    output_img = draw(content, '/app/style_images/picasso.jpg')
    return NdarrayToBase64(output_img)

@app.route('/gogh/<content>')
def gogh(content):
    content = Base64ToNdarry(content_base64)
    output_img = draw(content, '/app/style_images/gogh.png')
    return NdarrayToBase64(output_img)

@app.route('/munch/<content>')
def munch(content):
    content = Base64ToNdarry(content_base64)
    output_img = draw(content, '/app/style_images/munch.jpg')
    return NdarrayToBase64(output_img)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
