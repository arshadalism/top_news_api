# FastAPI application for top news using redis.

This application fetches the top news from hacker api and caches then for 10 minutes.

# Technologies Used-
    FastAPI - Backend framework to build the API.
    Redis - Used for caching the top news for quick response upto 10 minutes.
    Docker - Containerization of the application
    Docker Compose - Simplifies running the application with Redis.

# Prerequisites
    Docker - Ensure Docker is installed on your machine.

# Setup-
    First, clone this repo and build the Docker images for the project:
        $ git clone https://github.com/arshadalism/top_news_task.git
        $ cd top_news_task
        $ docker-compose build


# Running the API

    The docker-compose.yaml file in this project configures containers for a Redis instance with the RedisTimeSeries module, the Python app for the example API, and a test runner.
    Use this command to run all three containers:

    $ docker-compose up
    This command starts Redis and the API server and runs the tests.

# Top news data
    /top_news/{count} endpoint exists that fetches the top news from the api.

    $ curl -X GET http://127.0.0.1:8000/top_news/10

    Response - "[41277014, 41275920, 41276605, 41277429, 41262043, 41279691, 41275846, 41275759, 41263855, 41242095]"
    Above is the ids of the 10 news that we have fetched from hacker api.


# fastapi-news-app/
    ├── app/
    │   ├── __init__.py
    │   └── main.py
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    └── README.md


# Running in Development Mode
    To run the application in development mode with hot-reloading, you can use the following command:
    docker-compose up --build




