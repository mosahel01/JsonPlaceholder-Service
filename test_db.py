import psycopg

connection = psycopg.connect( # connection represents open convo with DB
    dbname="todo_app",
    user="todo_app_user",
    password="todo_password",
    host="localhost",
    port=5432,
)

# cursor = connection.cursor()
# cursor.execute(...)
# fetchall()