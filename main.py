import os

import Inference
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload_show.html', title_text="Hi, you can swap person's gender here")

@app.route('/', methods=['POST'])
def upload_image_female():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upl_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upl_path)
        print(upl_path)
        aligned = Inference.align(upl_path)
        male_filename = 'male_swapped' + filename
        female_filename = 'female_swapped' + filename
        Inference.transfer_style("model_checkpoints/to_male_net_G.pth", aligned, male_filename)
        Inference.transfer_style("model_checkpoints/to_female_net_G.pth", aligned, female_filename)
        flash('Image successfully transformed and displayed below')
        return render_template('upload_show.html',
                               filename_male=male_filename, filename_female=female_filename, title_text="Success!")
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run(host='0.0.0.0')