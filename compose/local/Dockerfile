# Dockerfile-flask
# We simply inherit the Python 3 image. This image does
# not particularly care what OS runs underneath
FROM python:3.11-slim-buster
# Set an environment variable with the directory
# where we’ll be running the app
# Create the directory and instruct Docker to operate
# from there from now on
WORKDIR /app
# Copy the requirements file in order to install
# Python dependencies
COPY requirements/base.txt .

# Install Python dependencies
RUN pip install -r base.txt
RUN pip install flask-jwt-extended
RUN pip install "PyJWT==2.1.0"

COPY . .
# Finally, we run uWSGI with the ini file we
# created earlier
EXPOSE 5000

#CMD [ "flask", "run"]
# Make Entrypoint executable
RUN chmod +x entrypoint.sh

CMD ["/bin/bash", "entrypoint.sh"]