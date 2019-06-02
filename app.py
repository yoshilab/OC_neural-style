import os
import cv2
import json
import numpy as np

from flask import Flask, request, render_template, send_file, url_for, jsonify
import base64, datetime
import neural_style as ns

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
    size = (560, 420)
    resize_data = cv2.resize(data, size)
    cv2.imwrite('/app' + img_path, resize_data)
    return img_path

def draw(content, style, output):
    #gan = ns.Gan()
    #generate_img = gan.generate(content, style, output)
    ns.generate(content, style, output)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images/<path:path>')
def get_image(path):
    return send_file('images/' + path)

@app.route('/picasso', methods=['POST'])
def picasso():
    content_base64 = request.form['image']
    content = Base64ToNdarry(content_base64)
    filename = create_filename()
    capture_img_path = save_image(content, '/images/input', 'cap_' + filename)
    #output = './output_images/picasso_' + content
    #generate_img = cv2.cvtColor(content, cv2.COLOR_BGR2GRAY)
    generate_img_path = '/images/output/pcs_' + filename
    draw('/app' + capture_img_path, '/app/style_images/picasso.jpg', '/app' + generate_img_path)
    res = {
        'org_url' : capture_img_path,
        'gen_url'  : generate_img_path
    }
    return jsonify(res)

@app.route('/gogh', methods=['POST'])
def gogh():
    content_base64 = request.form['image']
    content = Base64ToNdarry(content_base64)
    filename = create_filename()
    capture_img_path = save_image(content, '/images/input', 'cap_' + filename)
    #output = './output_images/picasso_' + content
    generate_img_path = '/images/output/ggh_' + filename
    draw('/app' + capture_img_path, '/app/style_images/gogh.png', '/app' + generate_img_path)
    res = {
        'org_url' : capture_img_path,
        'gen_url' : generate_img_path
    }
    return jsonify(res)

@app.route('/munch', methods=['POST'])
def munch():
    content_base64 = request.form['image']
    content = Base64ToNdarry(content_base64)
    filename = create_filename()
    capture_img_path = save_image(content, '/images/input', 'cap_' + filename)
    #output = './output_images/picasso_' + content
    generate_img_path = '/images/output/mnc_' + filename
    draw('/app' + capture_img_path, '/app/style_images/munch.jpg', '/app' + generate_img_path)
    res = {
        'org_url' : capture_img_path,
        'gen_url' : generate_img_path
    }
    return jsonify(res)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
