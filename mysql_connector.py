import mysql.connector

class mysql_helper:

    def db_connect(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="user_name",
            passwd="user_password",
            database="db_name"
        )
        cursor = connection.cursor(buffered=True)
        return connection, cursor
