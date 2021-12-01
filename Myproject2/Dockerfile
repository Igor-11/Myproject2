FROM python:3.10
MAINTAINER Shevchenko Ihor
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD exec gunicorn Myproject2.wsgi:application --bind 127.0.0.1:8000 --workers 3

