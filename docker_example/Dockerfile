### 1. Use offical Python images of choice
FROM python:3.8

### 1. Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

### 2. Create a working dir in docker container called src & copy app.py
WORKDIR /src
COPY ./app.py .

### 3. Install dependancies inside docker container
RUN set -e; \
    /usr/local/bin/python -m pip install --upgrade pip ;\
    python -m pip install --default-timeout=100 flask==2.2.3 ;

### 4. Set Flask env
ENV FLASK_APP=app

### 5. fire up flask app
ENTRYPOINT ["python","app.py"]