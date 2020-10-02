#use the python3.7.2 container image
FROM python:3.7.2-stretch

# Set the work directory to /app
WORKDIR /app

#Copy the current directory contents into the container at the /app
ADD . /app

#Install the dependencies
RUN pip install -r requirements.txt

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]