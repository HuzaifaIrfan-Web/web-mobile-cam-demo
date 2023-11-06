

from distutils.log import debug
from fileinput import filename
from flask import render_template, request, Flask
from flask import send_from_directory


# import module
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        # get current date and time
        current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        saved_file_name = f"{current_datetime}.jpg"
        saved_file_location = f"uploads/{saved_file_name}"
        f.save(saved_file_location)
        return render_template("uploaded.html", saved_file_location=saved_file_location)


@app.route('/uploads/<path:path>')
def send_uploads(path):
    return send_from_directory('uploads', path)


if __name__ == '__main__':
    app.run(debug=True)
