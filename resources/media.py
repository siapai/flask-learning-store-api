import os.path
from werkzeug.utils import secure_filename
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError


from db import db
from schemas import MultipartFileSchema

blp = Blueprint("Media", __name__, description="Operations on media")


@blp.route("/media/upload")
class Media(MethodView):

    @blp.arguments(MultipartFileSchema, location="files")
    @blp.response(201)
    def post(self, files):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_1 = files["file_1"]
        file_1.save(os.path.join(current_dir, "..", "uploads", secure_filename(file_1.filename)))
        return {"message": "Uploaded successfully."}

