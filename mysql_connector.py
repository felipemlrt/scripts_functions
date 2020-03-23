import mysql.connector

class mysql_helper:

    # connect function, to be used every time the database will be acessed
    # função de conexão a database, deve ser usada sempre que a database será acessada
    def db_connect(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="user_name",
            passwd="user_password",
            database="db_name"
        )
        cursor = connection.cursor(buffered=True)
        return connection, cursor
