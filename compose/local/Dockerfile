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
COPY requirements/ .

# Install Python dependencies
RUN pip install -r requirements/base.txt
# We copy the rest of the codebase into the image
COPY . .
# Finally, we run uWSGI with the ini file we
# created earlier
EXPOSE 5000

#CMD [ "executable" ] [ "flask", "run","--host","0.0.0.0","--port","5000"]
# Make Entrypoint executable
RUN chmod +x entrypoint.sh

CMD ["/bin/bash", "entrypoint.sh"]