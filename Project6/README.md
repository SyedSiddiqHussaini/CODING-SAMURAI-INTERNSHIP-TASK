# ✍️ SSH Blogs – Personal Blogging Platform
A personal blogging web application developed using **Python Flask** as part of my Python development learning journey.
The application allows users to register, log in, create blog posts, edit and delete their posts, and interact through a feedback system.

## 📌 Project Overview
SSH Blogs is a Flask-based web application designed to provide a simple blogging platform with user authentication and database integration.
It uses Flask for backend development, SQLite for data storage, Flask-SQLAlchemy for database operations, and Flask-Login for user session management.

## ✨ Features
### 👤 User Authentication
* User registration.
* User login and logout.
* Password hashing using Werkzeug.
* Login-protected dashboard.

### 📝 Blog Management
* Create new blog posts.
* View published blog posts.
* Edit existing posts.
* Delete personal posts.
* Restrict editing and deletion to post owners.

### 💬 Feedback System
* Submit feedback through a form.
* Store feedback in the SQLite database.
* Display submitted feedback on the home page.

### 📄 Additional Features
* Contact page.
* Resume download functionality.
* Dynamic HTML rendering using Flask templates.

## 🛠️ Technologies Used
| Technology       | Purpose                          |
| ---------------- | -------------------------------- |
| Python           | Backend programming              |
| Flask            | Web application framework        |
| Flask-SQLAlchemy | Database integration             |
| SQLite           | Database management              |
| Flask-Login      | User authentication and sessions |
| Werkzeug         | Password hashing                 |
| HTML & CSS       | Frontend development             |
| Jinja2           | Dynamic template rendering       |

## 📂 Project Structure
```text
project 6/
│
├── app.py
├── requirements.txt
├── templates/
├── static/
└── screenshots/
```

## 🚀 Installation and Setup
### 1. Clone the Repository
```bash
git clone https://github.com/SyedSiddiqHussaini/CODING-SAMURAI-INTERNSHIP-TASK.git
```
### 2. Navigate to Project 6
```bash
cd "CODING-SAMURAI-INTERNSHIP-TASK/project 6"
```
### 3. Create a Virtual Environment
```bash
python -m venv venv
```
Activate it:
**Windows:**
```bash
venv\Scripts\activate
```
**Linux / macOS:**
```bash
source venv/bin/activate
```
### 4. Install Dependencies
```bash
pip install flask flask-sqlalchemy flask-login
```
### 5. Run the Application
```bash
python app.py
```
Open your browser and visit:
```text
http://127.0.0.1:5000
```

## 📚 What I Learned
Through this project, I gained practical experience with:
* Building web applications using Flask.
* Understanding backend routing.
* Implementing user registration and authentication.
* Hashing passwords.
* Integrating SQLite databases.
* Performing CRUD operations.
* Managing user sessions.
* Working with HTML templates and dynamic content.

## 👨‍💻 Author
**Syed Siddiq Hussaini**
[GitHub Profile](https://github.com/SyedSiddiqHussaini)

⭐ Feel free to explore the project!
