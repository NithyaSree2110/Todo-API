# Todo API

A simple CRUD REST API built using **FastAPI** and **Python 3.12**.

---

## Features

- Create Tasks
- Read All Tasks
- Read Task by ID
- Update Tasks
- Delete Tasks
- Automatic Swagger Documentation

---

## Installation

Clone the repository:

```bash
git clone https://github.com/NithyaSree2110/Todo-API.git
cd Todo-API
```

Install dependencies:

```bash
pip install "fastapi[standard]"
```

---

## Run the API

```bash
fastapi dev main.py
```

or

```bash
uvicorn main:app --reload
```

The server will start at:

```
http://localhost:8000
```

---

## API Documentation

Swagger UI:

```
http://localhost:8000/docs
```

ReDoc:

```
http://localhost:8000/redoc
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get task by ID |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

---

## Sample curl Output

Delete a task:

```bash
curl -i -X DELETE http://localhost:8000/tasks/1
```

Response:

```http
HTTP/1.1 204 No Content
Date: Mon, 27 Jul 2026 10:18:02 GMT
Server: uvicorn
```

---

## Swagger UI
<img width="1450" height="956" alt="image" src="https://github.com/user-attachments/assets/3c93c4d8-a599-4409-b439-459b1d20c465" />
<img width="1438" height="965" alt="image" src="https://github.com/user-attachments/assets/ea465696-78ca-45d4-910e-c7558ef866e4" />
<img width="1451" height="966" alt="image" src="https://github.com/user-attachments/assets/df6169ba-6593-4193-be54-d929027425f7" />

