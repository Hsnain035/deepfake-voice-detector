from flask import Flask, render_template, request
import os
from model import predict_audio
import threading

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

result = ""

def run_prediction(path):
    global result
    result = predict_audio(path)

@app.route("/", methods=["GET", "POST"])
def home():
    global result

    if request.method == "POST":

        if 'audio' not in request.files:
            return "No file uploaded"

        file = request.files['audio']

        if file.filename == "":
            return "No selected file"

        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

        file.save(path)

        thread = threading.Thread(target=run_prediction, args=(path,))
        thread.start()
        thread.join()

        return render_template("index.html", prediction=result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)