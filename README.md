# Property Pursuit 🏠

Property Pursuit is a Django-based Real Estate Management System developed as part of a 1-year internship project. The application allows users to manage and explore property listings through a simple, secure, and user-friendly web interface.

## 📌 Project Overview

The objective of this project is to design and develop a functional real estate platform using Django that demonstrates core full-stack development concepts such as authentication, database integration, CRUD operations, and deployment-ready configuration.

## 🚀 Features

- User Authentication (Login & Registration)
- Property Listing Management
- Add, Edit, and Delete Properties
- Admin Panel for Full Control
- Responsive User Interface
- Secure Backend with Django Framework

## 🛠 Tech Stack

- Backend: Django (Python)
- Database: MySQL (via XAMPP)
- Frontend: HTML, CSS, Bootstrap
- Version Control: Git & GitHub
- Tools: VS Code / PyCharm

## 📂 Project Structure

  Property Pursuit/
├── 1-year project internship/
│ └── realestate/
│ ├── realestate/
│ ├── apps/
│ ├── templates/
│ ├── static/
│ └── manage.py
├── requirements.txt
├── README.md
└── Property Pursuit _Presentation.pptx

## ⚙️ Installation & Setup

Follow the steps below to run the project locally:

### 1️⃣ Clone the Repository
git clone https://github.com/Divya260406/Property-Pursuit.git

### 2️⃣ Navigate to Project Directory
cd Property-Pursuit

### 3️⃣ Create Virtual Environment
python -m venv venv

### 4️⃣ Activate Virtual Environment
venv\Scripts\activate

### 5️⃣ Install Dependencies
pip install -r requirements.txt

## 🗄️ Database Setup (XAMPP)

This project uses **MySQL via XAMPP** as the database.

Follow these steps carefully before running migrations:

1. Install and open **XAMPP Control Panel**
2. Start the following services:
   - Apache
   - MySQL

3. Click on **MySQL → Admin** to open **phpMyAdmin**
4. Create a new database with the name:
   realestate

5. Ensure your Django `settings.py` database configuration matches the following:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'realestate',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

## 🧩 Run Migrations

After creating the database, run the following commands:

python manage.py makemigrations  
python manage.py migrate

This will automatically create all required tables inside the **realestate** database.

## ▶️ Run the Development Server

python manage.py runserver

Open your browser and visit:  
http://127.0.0.1:8000/

## 🔐 Environment Variables

A `.env` file can be used to store sensitive information such as secret keys and database credentials (recommended for deployment).

## 📈 Future Enhancements

- Advanced property search and filtering
- User dashboard
- Property image uploads
- Role-based access control
- Cloud deployment
