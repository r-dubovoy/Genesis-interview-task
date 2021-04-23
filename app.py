from flask import Flask

UPLOAD_FOLDER = 'static/uploads/'
RENDER_MALE_FOLDER = 'static/transformMale/'
RENDER_FEMALE_FOLDER = 'static/transformFemale/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RENDER_MALE_FOLDER'] = RENDER_MALE_FOLDER
app.config['RENDER_FEMALE_FOLDER'] = RENDER_FEMALE_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024