# 🔗 Django URL Shortener

A simple URL shortener built using Django. It allows users to input long URLs and returns shortened versions, which can be used to redirect to the original URL.

## 📌 Features

- Generate short URLs for any valid long URL
- Automatic redirection from short to long URL
- Track number of times a short link is used
- Clean UI using Django templates

## 🚀 Getting Started

### 1. Clone the Repository

## ```bash
git clone https://github.com/student-Abhijit/url_shortner.git
cd url_shortner
## 2. Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
# or
source venv/bin/activate  # For Linux/macOS
## 3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
## 4. Apply Migrations
bash
Copy
Edit
python manage.py migrate
## 5. Run the Development Server
bash
Copy
Edit
python manage.py runserver
Now open your browser and go to http://127.0.0.1:8000/
