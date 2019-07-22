import os
import cv2
import json
import numpy as np

from flask import Flask, request, render_template, send_file, url_for, jsonify
import base64, datetime
#import neural_style as ns
import evaluate as fs

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

def create_filename():
    dt = datetime.datetime.today()
    dt_formatted = dt.strftime("%Y%m%d%H%M%S")
    extension = '.png'
    return dt_formatted + extension

def save_image(data, dir, filename):
    img_path = os.path.join(dir, filename)
    size = (480, 360)
    resize_data = cv2.resize(data, size)
    cv2.imwrite('/app' + img_path, resize_data)
    return img_path

@app.route('/')
def index():
    return render_template('fastns.html')
    #return render_template('index.html')

@app.route('/images/<path:path>')
def get_image(path):
    return send_file('images/' + path)

@app.route('/draw/<style>', methods=['POST'])
def draw(style):
    content_base64 = request.form['image']
    content = Base64ToNdarry(content_base64)
    checkpoint = './checkpoint/' + style + '.ckpt'
    file_in = './images/input_' + create_filename()
    file_out = './images/output.png'
    cv2.imwrite(file_in, content)
    output = fs.generate(checkpoint, file_in, file_out)

    try:
        os.remove(file_in)
    except:
        print('Not found content file.')
    
    height = output.shape[0]
    width = output.shape[1]
    output_re = cv2.resize(output , (int(width*1.5), int(height*1.5)))
    generate_img = 'data:image/png;base64,' + NdarrayToBase64(output_re)
    res = {
        'generate_img'  : generate_img
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
