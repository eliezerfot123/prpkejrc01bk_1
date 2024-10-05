# qaroni

## Docker Quickstart

This app can be run completely using `Docker` and `docker compose`. **Using Docker is recommended, as it guarantees the application is run using compatible versions of Python and Node**.

There are three main services:

To run the development version of the app

```bash
docker compose -f docker-compose.yml build --no-cache
```

To run the production version of the app

```bash
docker compose -f docker-compose.yml up -d 
```

### Running locally

Run the following commands to bootstrap your environment if you are unable to run the application using Docker

preview install and configure your db, for example linux;
```bash
createdb qaroni -O youruser

```

configure your file .env as .env.example and add your configurate for email and db

now configure your enviroment

```bash
cd qaroni
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements/base.txt
flas run
```

Go to `http://localhost:5000`. You will see a pretty welcome screen.

#### Database Initialization (locally)

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration

```bash
flask db migrate
flask db upgrade
```





