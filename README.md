# Property Pursuit 🏠

Property Pursuit is a Django-based Real Estate Management System developed as part of a 1-year internship project. The application allows users to browse, add, manage, and maintain property listings through a clean and user-friendly web interface.

## 📌 Project Overview

The goal of this project is to build a functional real estate platform that demonstrates full-stack web development skills using Django. It covers core backend concepts such as authentication, database integration, CRUD operations, and deployment-ready configuration.

## 🚀 Features

- User Authentication (Login & Registration)
- Property Listing Management
- Add, Edit, and Delete Properties
- Admin Panel for Full Control
- Responsive User Interface
- Secure Backend with Django Framework

## 🛠 Tech Stack

- Backend: Django (Python)
- Database: MySQL / MariaDB
- Frontend: HTML, CSS, Bootstrap
- Version Control: Git & GitHub
- Tools: VS Code / PyCharm

## 📂 Project Structure

Property Pursuit/
├── 1-year project internship/
│   └── realestate/
│       ├── realestate/
│       ├── apps/
│       ├── templates/
│       ├── static/
│       └── manage.py
├── requirements.txt
├── README.md
└── Property Pursuit _Presentation.pptx

## ⚙️ Installation & Setup

Follow the steps below to run the project locally:

1. Clone the repository  
git clone https://github.com/Divya260406/Property-Pursuit.git

2. Navigate to project directory  
cd Property-Pursuit

3. Create a virtual environment  
python -m venv venv

4. Activate the virtual environment  
venv\Scripts\activate

5. Install dependencies  
pip install -r requirements.txt

6. Apply migrations  
python manage.py makemigrations  
python manage.py migrate

7. Run the development server  
python manage.py runserver

Open your browser and visit:  
http://127.0.0.1:8000/

## 🔐 Environment Variables

A `.env` file can be used to store sensitive information such as secret keys and database credentials (recommended for deployment).

## 📈 Future Enhancements

- Advanced property search and filters
- User dashboard
- Image upload support for properties
- Role-based access control
- Cloud deployment
