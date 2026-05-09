from flask import Blueprint
from flask import request
from flask import jsonify

from app.extensions import db
from app.extensions import socketio
from flask import render_template
from flask import redirect

from app.models.task import Task

from app.utils.analytics import (
    calculate_analytics
)

task_bp = Blueprint(
    "tasks",
    __name__
)

@task_bp.route("/tasks", methods=["POST"])
def create_task():

    data = request.get_json()

    title = data.get("title")

    description = data.get("description")

    priority = data.get("priority")

    status = data.get("status")

    user_id = data.get("user_id")

    new_task = Task(
        title=title,
        description=description,
        priority=priority,
        status=status,
        user_id=user_id
    )

    db.session.add(new_task)

    db.session.commit()

    socketio.emit(
        "task_created",
        {
            "message": "New task created",
            "task": {
                "id": new_task.id,
                "title": new_task.title,
                "status": new_task.status
            }
        }
    )
    analytics = calculate_analytics()
 
    socketio.emit(
       "analytics_updated",
       analytics
)
    

    return jsonify({
        "message": "Task created successfully"
    }), 201

@task_bp.route("/tasks", methods=["GET"])
def get_tasks():

    tasks = Task.query.all()

    task_list = []

    for task in tasks:

        task_list.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "status": task.status,
            "created_date": task.created_date
        })

    return jsonify(task_list), 200

@task_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    task = Task.query.get(task_id)

    if not task:
        return jsonify({
            "error": "Task not found"
        }), 404

    data = request.get_json()

    task.title = data.get(
        "title",
        task.title
    )

    task.description = data.get(
        "description",
        task.description
    )

    task.priority = data.get(
        "priority",
        task.priority
    )

    task.status = data.get(
        "status",
        task.status
    )

    db.session.commit()

    socketio.emit(
        "task_updated",
        {
            "message": "Task updated",
            "task_id": task.id
        }
    )

    analytics = calculate_analytics()

    socketio.emit(
       "analytics_updated",
       analytics
)
    return jsonify({
        "message": "Task updated successfully"
    }), 200

@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    task = Task.query.get(task_id)

    if not task:
        return jsonify({
            "error": "Task not found"
        }), 404

    db.session.delete(task)

    db.session.commit()

    socketio.emit(
        "task_deleted",
        {
            "message": "Task deleted",
            "task_id": task.id
        }
    )
    analytics = calculate_analytics()

    socketio.emit(
      "analytics_updated",
       analytics
)
    

    return jsonify({
        "message": "Task deleted successfully"
    }), 200

@task_bp.route("/")
def home():

    return redirect("/login-page")

@task_bp.route("/dashboard")
def dashboard():

    return render_template(
        "index.html"
    )