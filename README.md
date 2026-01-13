# Conference Room Reservation App

Conference Room Reservation App is a web application developed with Django for managing conference room reservations.  
The project focuses on backend logic, database integration and application configuration, simulating a real-world booking system.

This application was developed as a personal project to practice backend development with Django and relational databases.

---

## Features

- Create and manage conference rooms
- Book conference rooms for specific dates
- Backend logic implemented with Django
- Database integration using Django ORM
- Environment-based configuration using `local_settings.py`

---

## Technologies Used

- Python
- Django
- HTML
- CSS
- Relational Database (PostgreSQL or SQLite)
- Git

---

## Project Structure

- Django project structure with apps, models and views
- Configuration separated between main settings and local settings
- Database migrations handled via Django ORM

---

## Run Locally

Follow these steps to run the project on your local machine:

### 1. Clone the repository
```bash
git clone https://github.com/Daviz96/Conference-Room-Reservation-App.git
cd Conference-Room-Reservation-App
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment settings
Create a file named `local_settings.py` inside the project directory and add:

```python
SECRET_KEY = 'your-secret-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
```

*(PostgreSQL can also be configured if preferred.)*

---

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Run the development server
```bash
python manage.py runserver
```

Open your browser at:
```
http://127.0.0.1:8000/
```

---

## Purpose of the Project

The goal of this project was to:
- Practice backend development with Django
- Work with relational databases and ORM
- Understand project configuration and environment separation
- Build a realistic web application for booking management

---

## Author

Developed by **Dawid Sebastian Wrzesiński**

GitHub: https://github.com/Daviz96

