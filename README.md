# Mind Me - Mental Health Assistance System

Mind Me is an innovative platform designed to help individuals with mental distress by assessing their mental state through MCQ-based and image-based questions. Based on their responses, the system provides tailored solutions such as chatbot interaction with caretakers, stress-relief music, and engaging games.

## Features
- **Mental State Assessment**: Users answer MCQ-based and image-based questions to determine their mental well-being.
- **Personalized Recommendations**: Based on responses, the system provides stress-relief activities such as:
  - Chatbot interaction with caretakers
  - Calming music suggestions
  - Stress-relief games
- **User-Friendly Interface**: Designed with an intuitive and engaging UI/UX for seamless navigation.

## Tech Stack
- **Frontend**: Django Templates, HTML, CSS, JavaScript
- **Backend**: Django 5.0.6 (Python)
- **Database**: SQLite
- **AI/ML Integration**: Python-based image processing
- **Other Tools**: Chatbot integration for user support
- **CORS**: django-cors-headers for cross-origin requests

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Praveenvin/mindme.git
   cd mindme-1
   ```

2. Create a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install Django==5.0.6 django-cors-headers
   ```

4. Navigate to the Django project directory:
   ```sh
   cd mindme
   ```

5. Run migrations to initialize the database:
   ```sh
   python manage.py migrate
   ```

6. (Optional) Create a superuser for admin access:
   ```sh
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```sh
   python manage.py runserver
   ```

8. Open your browser and navigate to:
   ```
   http://localhost:8000/
   ```

## Contribution
We welcome contributions! Feel free to fork the repository, create a new branch, and submit a pull request.
