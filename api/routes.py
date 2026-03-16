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

@main.route("/snippets", methods=["GET"])
def get_snippets():

    snippets = db.snippets.find({}, {
        "title": 1,
        "code": 1,
        "language": 1,
        "description": 1
    })

    data = []

    for snippet in snippets:
        data.append({
            "id": str(snippet["_id"]),
            "title": snippet.get("title"),
            "language": snippet.get("language"),
            "code": snippet.get("code"),
            "description": snippet.get("description")
        })

    return jsonify(data)