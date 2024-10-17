
# Quizora

<p align="center">
  <img src="Github/assets/images/quizora_main.png" alt="Quizora Logo" width="300">
</p>

An interactive educational quiz app designed to engage and educate!

## Overview

Quizora is a feature-rich quiz application built using Django, designed to offer an engaging and interactive quiz experience. It includes user authentication, session tracking, and a dynamic leaderboard that encourages friendly competition. This project was developed for thee AlX Program Final Project to demonstrate and sharpen web development skills with a focus on Python, Django, HTML/CSS, and JavaScript.

## Features

- **Authentication System:** Users can register, log in, and manage their profiles.
- **Interactive Quizzes:** Timed quizzes with immediate feedback on answers.
- **Leaderboard:** Displays the top-performing users with their profile images.
- **Responsive Design:** Works seamlessly across different devices.
- **REST API Support:** Quiz questions served through Django REST framework.
- **Session Management:** Tracks user progress and quiz attempts.

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** Bootstrap, HTML5, CSS3, JavaScript
- **Database:** SQLite (Development) / PostgreSQL (Deployment)
- **Deployment:** Render (Host)

## Logo Showcase

<p align="center">
  <img src="Github/assets/images/quizora_logo.jpg" alt="Quizora Logo with Tech Icons" width="400">
</p>

## Installation and Setup

### Prerequisites

- Python 3.8+ installed
- pip (Python package installer)
- A virtual environment for dependency management (recommended)

### Step-by-Step Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Tweek-byte/Quiz-App
   cd Quizora
   ```

2. **Create a virtual environment and activate it:**

   **On macOS/Linux:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   **On Windows:**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations to set up the database:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser to access the admin panel:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files (for production):**

   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## Usage

- **Access the Homepage:** Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to start using Quizora.
- **Admin Panel:** Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to manage quizzes, users, and results.
- **Leaderboard:** Check the top users on the leaderboard page for some friendly competition.

## Project Structure

```
Quiz_Application_Project/
├── Quizora/                 # Django project root
├── homepage/                # Homepage app
├── media/                   # User-uploaded media (e.g., profile images)
├── quiz/                    # Quiz functionality app
├── session/                 # User session management
├── static/                  # Static files (CSS, JS)
├── staticfiles/             # Collected static files for deployment
├── templates/               # HTML templates
├── .gitignore               # Files to ignore in version control
├── README.md                # Documentation
├── manage.py                # Django management script
└── requirements.txt         # Dependencies

```

5. **Handle static files:**

   ```bash
   python manage.py collectstatic --noinput
   ```

## Author

**Zakaria Aabab**  
📧 Email: [zakariaaabab@gmail.com](mailto:zakariaaabab@gmail.com)


## Future Improvements

- **Switch to PostgreSQL:** For better scalability and performance.
- **Add Social Login:** Enable users to log in with Google or Facebook.
- **Implement Quiz Categories:** Offer quizzes by topic or difficulty level.
- **Mobile App Version:** Develop a mobile app for iOS and Android.

## License
    ```Project is protected under license
    ```