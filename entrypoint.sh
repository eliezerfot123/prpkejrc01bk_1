rm -rf migrations
flask db init
flask db migrate
flask db upgrade
flask run --host=0.0.0.0 --port=5000