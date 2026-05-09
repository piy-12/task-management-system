from datetime import datetime

from app.extensions import db

class Task(db.Model):

    __tablename__ = "tasks"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    priority = db.Column(
        db.String(20),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="PENDING"
    )

    created_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )