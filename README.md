# StudyLab Django Project Setup

This README provides the steps to run Tha StudyLab Django project.

For [Video Demonstration](https://drive.google.com/file/d/13NWfWFfjEEKecvuOuang1BmBBYI1Iosp/view?usp=sharing) 

Blog Link of Project: [Blog](https://medium.com/@emmanuelgudinho45/revolutionize-learning-with-smart-education-system-generative-ai-django-and-pwa-integration-b5024e6702e3)

**Reason for these many Apps** : Creating different apps for different features in Django promotes modularity, reusability, and maintainability of the codebase.


## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Create a Virtual Environment**:
    - On macOS and Linux:
        ```bash
        python3 -m venv env
        ```
    - On Windows:
        ```bash
        python -m venv env
        ```

2. **Activate the Virtual Environment**:
    - On macOS and Linux:
        ```bash
        source env/bin/activate
        ```
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```

3. **Install Project Dependencies**:
    - With the virtual environment activated, install the project dependencies using pip:
        ```bash
        pip install -r requirements.txt
        ```

## Running the Project

1. **Set Environment Variables**:
    - Set up .env
    - Get the Google [Gemini Api Key](https://ai.google.dev/gemini-api)


2. **Apply Migrations**:
    - Apply the database migrations using Django's management command:
        ```bash
        python manage.py migrate
        python manage.py makemigrations
        ```

3. **Start the Development Server**:
    - Django comes with a built-in development server.
        ```bash
        python manage.py runserver
        ```

4. **Visit the Application**:
    - Open your web browser and navigate to `http://127.0.0.1:8000/`.


