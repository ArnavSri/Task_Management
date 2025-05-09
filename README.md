# Task Management API

This is a Django REST Framework-based API for managing tasks and assigning them to users. It allows CRUD operations on tasks and users, as well as task assignments.

## Features

- Create task with task details.
- Fetch all the avaliable users details. 
- Assign a task to multiple user.
- Fetch all tasks assigned to a user.

## Technologies Used

- Python,Django
- Django REST Framework
- SQLite (Default Database, can be changed)
- Postman (for API testing)

## Installation part 

- Install Python using powershell
- Then check pip install is there using pip --version
- Then install Django using pip install django 
- Then install Django Restframework using pip install django djangorestframework

## Setup the project in VSCode 

- Then create a folder open in VSCode 
- After that using below mention command to setup the project 

```sh
    django-admin startproject task_manager
    python manage.py startapp tasks
``` 

---

## Setup the project 

### 1. Clone the Repository

```sh
    git clone <repository-url>
    cd <project-directory>
```

### 2. Create a Virtual Environment & Activate It

```sh
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
```

### 3. Install Dependencies

```sh
    pip install -r requirements.txt
```

### 4. Apply Migrations

```sh
    python manage.py makemigrations
    python manage.py migrate
```

### 5. Create a Superuser (For Admin Access)

```sh
    python manage.py createsuperuser
    # Follow the prompts to set username & password
```

### 6. Run the Server

```sh
    python manage.py runserver
```

---

## API Endpoints

### **1. Task Endpoints**

#### Create a Task

```
POST /api/tasks/
```

**Request Body:**

```json
{
    "task_name": "Fix Login Bug",
    "description": "Fix the issue causing login failures",
    "task_type": "Bug"
}
```

---

### **2. User Endpoints**

#### List All Users

```
GET /api/users/
```

### **3. Assign Task to Users**

```
POST /api/tasks/assign/
```

**Request Body:**

```json
{
    "task_id": 1,
    "user_ids": [2, 3]
}
```

**Response:**

```json
{
    "message": "Task assigned successfully",
    "task": {
        "task_id": 1,
        "task_name": "Fix Login Bug",
        "assigned_users": [
            { "user_id": 2, "username": "John Doe", "email": "john@example.com", "mobile": "9876543211" },
            { "user_id": 3, "username": "Alice", "email": "alice@example.com", "mobile": "9876543212" }
        ]
    }
}
```

---

### **4. Fetch Tasks Assigned to a User**

```
GET /api/users/{user_id}/tasks/
```

---

## Testing the API

Use **Postman** or **cURL** to test the API, or you can use Django’s built-in API browser by navigating to `http://127.0.0.1:8000/api/`

---

## Notes

- `task_type`, `completed_at`, and `status` have default values.
- The `assign_task_to_users` API ensures only valid users are assigned to tasks.

---

## Author

- **Arnav Srivastava**



