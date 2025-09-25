# Complaint Management System

A Django-based web application for submitting and tracking complaints, built with user authentication, a dashboard, and basic styling.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots/GIFs](#screenshotsgifs)
- [Contributing](#contributing)
- [License](#license)

## 1. Features
- User registration and login/logout functionality.
- Submit complaints with title, description, image, and location (latitude/longitude).
- Dashboard to view submitted complaints and daily statistics (via Chart.js).
- Responsive design with Tailwind CSS and custom styling.
- Session-based authentication with logout clearing.

## 2. Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sel20/complaint-management-system.git
   cd complaint-management-system
   
2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Note: Create a requirements.txt file with django==5.2.6 and other dependencies (e.g., pillow     for images) if not already present:
   ```bash
   pip freeze > requirements.txt
   
4. **Configure Settings**
 - Update cms_project/settings.py with your SECRET_KEY.
 - Ensure DEBUG = True for development (set to False for production).
 - Verify STATIC_URL, STATICFILES_DIRS, and STATIC_ROOT are set:
   ```python
   Update cms_project/settings.py with your SECRET_KEY.
 - Set authentication URLs:
   ```python
   LOGIN_URL = '/login/'
   LOGIN_REDIRECT_URL = '/'
   LOGOUT_REDIRECT_URL = '/login/'
   
5. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

6. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```
   Use testuser and Selwyn2025! as credentials for testing.

7. **Collect Static Files**
   ```bash
   python manage.py collectstatic

8. **Run the Server**
   ```bash
   python manage.py runserver
   ```
   Access the app at http://127.0.0.1:8000/.

## 3. Usage

1. Register: Visit http://127.0.0.1:8000/register/ to create an account.
2. Login: Use http://127.0.0.1:8000/login/ with testuser and Selwyn2025!.
3. Dashboard: After login, view your complaints and statistics at http://127.0.0.1:8000/.
4. Submit Complaint: Use the "Submit a Complaint" link to add new complaints.
5. Logout: Click "Logout" on the navbar to end the session.

## 4. Screenshots/GIFs

1. Login Page: <img width="1914" height="970" alt="image" src="https://github.com/user-attachments/assets/800d43c6-5352-407c-8900-cfddc989657a" />

2. Dashboard Flow 1: <img width="1916" height="917" alt="image" src="https://github.com/user-attachments/assets/c982bc63-2b6c-4f85-9e51-18b80f05a754" />
Dashboard Flow 2: <img width="1918" height="922" alt="image" src="https://github.com/user-attachments/assets/17f0e277-8fd9-46f3-968b-2e2b7d900a41" />
Dashboard Flow 3: <img width="1917" height="919" alt="image" src="https://github.com/user-attachments/assets/8e48a251-f42b-49aa-b23a-4e4e80d95c3c" />

3. Submit Complaint: <img width="1919" height="917" alt="image" src="https://github.com/user-attachments/assets/b48a6c44-388a-47d9-8c85-6fa47ff2d97e" />

4. Registering Page: <img width="1919" height="911" alt="image" src="https://github.com/user-attachments/assets/b7c1a8c1-c9b6-4149-a9c2-00d10d12e1f6" />


To add visuals:

## 5. Contributing

Feel free to fork this repository, submit issues, or create pull requests.
Contributions are welcome!

## 6. License
This project is licensed under the MIT License - see the LICENSE file for details.

