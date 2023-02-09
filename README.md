## Dash on flask with flask_login

1. Clone the repo:

   ```
   git clone
   ```

2. Setup some environment variables:

   ```
   cd into
   touch .env
   ```

3. and add this in the `.env` file:

   ```
   export FLASK_APP=dashapp
   export FLASK_DEBUG=True
   export DATABASE_URL=sqlite:///${PWD}/app.db
   export SECRET_KEY=secret_key_change_as_you_wish_make_it_long_123
   export MONGO_DB_URL=url_string_mongo_db
   ```

4. create a virtual enviroment and run

   ```
   pip install -r requirements.txt
   flaskflask db init
   flask db migrate -m 'init'
   flask db upgrade
   flask run
   ```

Finally create a user and jump into: http://127.0.0.1:5000/dashboard-company

## With Docker for development

Then build and run in detached mode with [`docker-compose`](https://docs.docker.com/compose/reference/up/) (you might need to `chmod +x entrypoint.sh` before running docker compose):

```
docker-compose up --build
```
