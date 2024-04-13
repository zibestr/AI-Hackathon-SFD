import os
from flask import Flask, request, render_template, redirect, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder=os.path.join(os.path.abspath("./"), "source/templates"))


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route('/get_file', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect("/result")
        

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template("result.html")


if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.abspath("./"), "data")
    app.run(port=8000)
