# YouTube Fetcher

This project is a Django application that fetches YouTube videos using the YouTube Data API and displays them on a dashboard. It uses Celery for periodic tasks.

## Prerequisites

- Python 3.8+
- PostgreSQL
- Redis
- pip (Python package installer)

## Setup

### Clone the Repository

```sh
git clone https://github.com/yourusername/youtube_fetcher.git
cd youtube_fetcher
```
Create a Virtual Environment

Windows
```
python -m venv venv
venv\Scripts\activate`
```
Linux
```
python3 -m venv venv
source venv/bin/activate
```

Install Dependencies
```pip install -r requirements.txt```

Add you youtube_api_key in `videos/tasks.py`.

### Configure the Database
Create a PostgreSQL database and user.
Update the DATABASES setting in `settings.py` with your `database credentials`.
Apply Migrations
```
python manage.py makemigration
python manage.py migrate
```
Create a Superuser
```
python manage.py createsuperuser
```
Run the Development Server
```
python manage.py runserver
```
### Start Redis Server
Windows
`Download and install Redis from https://github.com/microsoftarchive/redis/releases.`
or can use docker to start the redis server 
`docker run --name redis-server -d -p 6379:6379 redis`

Start Redis server:
```
redis-server
```

Linux
Install Redis:
```
sudo apt-get install redis-server
```
Start Redis server:
```
sudo service redis-server start
```
Start Celery Worker
```
celery -A youtube_fetcher worker --loglevel=info
```

Start Celery Beat
```
celery -A youtube_fetcher beat --loglevel=info
```
### Access the Application
Open your browser and go to `http://127.0.0.1:8000/admin` to access the Django admin panel.
Go to `http://127.0.0.1:8000/dashboard/videos` to view the video dashboard.

### Directory Structure
```
youtube_fetcher/
    manage.py
    videos/
        __init__.py
        admin.py
        apps.py
        migrations/
        models.py
        tasks.py
        templates/
            dashboard.html
        tests.py
        urls.py
        views.py
    youtube_fetcher/
        __init__.py
        asgi.py
        celery.py
        settings.py
        urls.py
        wsgi.py
```
Example 
![Screenshot (1241)](https://github.com/user-attachments/assets/560ef0a9-8a02-49e0-aac2-508c965613a6)

