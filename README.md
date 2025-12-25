# [BioGenerator]

> A brief description of what this project does and who it's for.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?style=flat&logo=django)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📖 About

**Bio Generator** is a web application designed to cure "About Me" writer's block. We all know that writing about yourself is one of the hardest things to do—whether it's for a LinkedIn profile, a Twitter header, or a personal portfolio.

This project automates that process. Users simply input their key details—such as their profession, hobbies, skills, and desired tone (Professional, Funny, Casual)—and the application generates a polished, ready-to-use biography. Built with **Django**, it streamlines the process of personal branding, making it easy for anyone to introduce themselves to the world.

## ✨ Features

* **User Authentication:** Secure login and registration.
* **Responsive Design:** Works on mobile and desktop.

## 🛠 Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite (Development) / PostgreSQL (Production)

## 🚀 Getting Started

Follow these instructions to set up the project locally on your machine.

### Prerequisites

Ensure you have Python installed on your system:
* Python 3.8+
* pip

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/codewithmittalhardik/Biogenerator.git]((https://github.com/codewithmittalhardik/Biogenerator.git)
    cd repo-name
    ```

2.  **Create a Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables**
    Create a `.env` file in the root directory and add the following:
    ```env
    SECRET_KEY=your_secret_key_here
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    ```

5.  **Run Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Create a Superuser (Optional)**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

    Open your browser and visit `http://127.0.0.1:8000/`.

## 📂 Project Structure

```text
├── project_name/       # Main Django configuration
├── app_name/           # Your specific app logic
├── static/             # CSS, Images, JS
├── templates/          # HTML files
├── manage.py           # Django command-line utility
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
