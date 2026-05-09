# task-management-system

## Features

- User Authentication
- Task CRUD APIs
- PostgreSQL Integration
- Real-time WebSocket Updates
- Pandas & NumPy Analytics
- Responsive Frontend

## Tech Stack

- Flask
- PostgreSQL
- SQLAlchemy
- Flask-SocketIO
- Pandas
- NumPy
- HTML/CSS/JavaScript

## Installation

### Clone Repository

git clone <repo-url>

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Configure Environment Variables

Create .env file:

DATABASE_URL=postgresql://postgres:password@localhost/taskdb

SECRET_KEY=your_secret_key

### Run Migrations

python -m flask db upgrade

### Start Server

python run.py

## API Endpoints

POST /register
POST /login

GET /tasks
POST /tasks
PUT /tasks/<id>
DELETE /tasks/<id>

GET /analytics

## WebSocket Events

- task_created
- task_updated
- task_deleted
- analytics_updated