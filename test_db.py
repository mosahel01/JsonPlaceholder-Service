import psycopg

connection = psycopg.connect( # connection represents open convo with DB
    dbname="todo_app",
    user="postgres",
    host="localhost",
    port=5432,
)