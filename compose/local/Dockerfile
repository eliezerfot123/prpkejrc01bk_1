# Dockerfile-flask
# We simply inherit the Python 3 image. This image does
# not particularly care what OS runs underneath
FROM python:3
# Set an environment variable with the directory
# where we’ll be running the app
ENV APP /app
# Create the directory and instruct Docker to operate
# from there from now on
RUN mkdir $APP
WORKDIR $APP
# Copy the requirements file in order to install
# Python dependencies
COPY . .

# Install Python dependencies
RUN pip install -r requirements/base.txt

# Finally, we run uWSGI with the ini file we
# created earlier
EXPOSE 5000

#CMD [ "flask", "run"]
# Make Entrypoint executable
#RUN chmod +x entrypoint.sh

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
CMD ["uwsgi", "--ini", "uwsgi.ini"]