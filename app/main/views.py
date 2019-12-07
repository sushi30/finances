import os
from flask import Blueprint, current_app as app, request
from werkzeug.utils import secure_filename

main = Blueprint("main", __name__)


@main.route("/version")
def index():
    return "0.0.1"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


ALLOWED_EXTENSIONS = {"xls", "csv", "xlsx"}


@main.route("/upload", methods=["POST"])
def upload():
    # check if the post request has the file part
    if "file" not in request.files:
        return "No file part", 400
    file = request.files["file"]
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == "":
        return "No selected file", 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return "", 201
