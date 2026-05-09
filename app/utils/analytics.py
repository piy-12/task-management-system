import pandas as pd
import numpy as np

from app.models.task import Task


def calculate_analytics():

    tasks = Task.query.all()

    task_data = []

    for task in tasks:

        task_data.append({

            "id": task.id,

            "title": task.title,

            "status": task.status,

            "priority": task.priority
        })

    df = pd.DataFrame(task_data)

    total_tasks = len(df)

    if total_tasks == 0:

        return {

            "total_tasks": 0,

            "completed_tasks": 0,

            "pending_tasks": 0,

            "completion_percentage": 0
        }

    completed_tasks = len(

        df[df["status"] == "COMPLETED"]
    )

    pending_tasks = len(

        df[df["status"] != "COMPLETED"]
    )

    completion_percentage = np.round(

        (completed_tasks / total_tasks) * 100,

        2
    )

    return {

        "total_tasks": int(total_tasks),

        "completed_tasks": int(completed_tasks),

        "pending_tasks": int(pending_tasks),

        "completion_percentage": float(
            completion_percentage
        )
    }