import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user='root'
)

try:
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE DATABASE processedfiles") ##currently placeholder!
except mysql.connector.Error as err:
    print("error with database: {}".format(err))
