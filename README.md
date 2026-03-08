# Placement Tracker Backend

Backend system built using **FastAPI and PostgreSQL** to manage company information and interview experiences for students preparing for campus placements.
Placement Tracker helps students **store, manage, and view interview experiences** of companies visiting their campus.  
It provides secure authentication and REST APIs for managing users, companies, and interview experience posts.

---
## Features
- User **signup and login** with JWT authentication
- Secure **password hashing using bcrypt**
- Create and manage **companies**
- Post and view **interview experiences**
- Request validation and proper **HTTP error handling**
- Interactive API documentation using **FastAPI Swagger**

---

## Tech Stack
- **FastAPI** – Backend framework
- **PostgreSQL** – Relational database
- **SQLAlchemy** – ORM for database operations
- **JWT** – Authentication
- **bcrypt** – Password hashing

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/placement-tracker.git
cd placement-tracker
pip install -r requirements.txt
uvicorn app.main:app --reload
http://127.0.0.1:8000/docs
```

<img width="1331" height="974" alt="Screenshot 2026-03-08 173845" src="https://github.com/user-attachments/assets/79ab44db-11b3-4c61-933d-256ef8346297" />
