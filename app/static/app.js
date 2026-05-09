const socket = io()

async function fetchTasks() {

    const response = await fetch("/tasks")

    const tasks = await response.json()

    const taskList = document.getElementById(
        "taskList"
    )

    taskList.innerHTML = ""

    let completed = 0

    tasks.forEach(task => {

        if (task.status === "COMPLETED") {
            completed++
        }

        taskList.innerHTML += `

<div class="task">

    <h3>${task.title}</h3>

    <p>${task.description}</p>

    <p>Priority: ${task.priority}</p>

    <p>Status: ${task.status}</p>

    <select onchange="updateTaskStatus(${task.id}, this.value)">

        <option value="PENDING"
            ${task.status === "PENDING" ? "selected" : ""}>
            PENDING
        </option>

        <option value="IN_PROGRESS"
            ${task.status === "IN_PROGRESS" ? "selected" : ""}>
            IN PROGRESS
        </option>

        <option value="COMPLETED"
            ${task.status === "COMPLETED" ? "selected" : ""}>
            COMPLETED
        </option>

    </select>

    <button onclick="deleteTask(${task.id})">
        Delete
    </button>

</div>
`
    })
}

async function fetchAnalytics() {

    const response = await fetch(
        "/analytics"
    )

    const data = await response.json()

    document.getElementById(
        "totalTasks"
    ).innerText = data.total_tasks

    document.getElementById(
        "completedTasks"
    ).innerText = data.completed_tasks

    document.getElementById(
        "pendingTasks"
    ).innerText = data.pending_tasks

    document.getElementById(
        "completionPercentage"
    ).innerText =
        data.completion_percentage + "%"
}

async function createTask() {

    const title = document.getElementById(
        "title"
    ).value

    const description = document.getElementById(
        "description"
    ).value

    const priority = document.getElementById(
        "priority"
    ).value

    await fetch("/tasks", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            title,
            description,
            priority,
            status: "PENDING",
            user_id: 1
        })
    })
}

async function deleteTask(taskId) {

    await fetch(`/tasks/${taskId}`, {

        method: "DELETE"
    })
}

socket.on(
    "task_created",
    () => {
        fetchTasks()
    }
)

socket.on(
    "task_updated",
    () => {
        fetchTasks()
    }
)

socket.on(
    "task_deleted",
    () => {
        fetchTasks()
    }
)

socket.on(
    "analytics_updated",
    (data) => {

        document.getElementById(
            "totalTasks"
        ).innerText = data.total_tasks

        document.getElementById(
            "completedTasks"
        ).innerText =
            data.completed_tasks

        document.getElementById(
            "pendingTasks"
        ).innerText =
            data.pending_tasks

        document.getElementById(
            "completionPercentage"
        ).innerText =
            data.completion_percentage + "%"
    }
)

async function updateTaskStatus(
    taskId,
    newStatus
) {

    await fetch(`/tasks/${taskId}`, {

        method: "PUT",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            status: newStatus
        })
    })
}

fetchTasks()
fetchAnalytics()