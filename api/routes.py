from flask import Blueprint, jsonify
from .db import db

main = Blueprint("main", __name__)

@main.route("/health")
def health():
    collections = db.list_collection_names()

    return jsonify({
        "status": "ok",
        "collections": collections
    })
