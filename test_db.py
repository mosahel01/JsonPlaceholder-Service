import psycopg

# opens a connection with PostgreSQL
connection = psycopg.connect( 
    dbname="todo_app",
    user="todo_app_user",
    password="todo_password",
    host="localhost",
    port=5432,
)

# create something that can execute SQL
cursor = connection.cursor() 

# send SQL query to PostgreSQL
cursor.execute(
    """
    INSERT INTO todos(title)
    VALUES ('Learn Docker');
    """
)

connection.commit()

print("Todo Inserted")

connection.close()

# # receives all the rows into python
# rows = cursor.fetchall()
#
# for row in rows:
#     print(row)