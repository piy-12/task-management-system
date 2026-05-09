from flask import Blueprint
from flask import request
from flask import jsonify

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from app.extensions import db

from app.models.user import User


auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")

    email = data.get("email")

    password = data.get("password")

    existing_user = User.query.filter_by(
        email=email
    ).first()

    if existing_user:
        return jsonify({
            "error": "User already exists"
        }), 400

    hashed_password = generate_password_hash(password)

    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)

    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    }), 201

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")

    password = data.get("password")

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:
        return jsonify({
            "error": "Invalid credentials"
        }), 401

    valid_password = check_password_hash(
        user.password,
        password
    )

    if not valid_password:
        return jsonify({
            "error": "Invalid credentials"
        }), 401

    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }), 200