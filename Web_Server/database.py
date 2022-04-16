import mysql.connector

config = {
    'user': 'root',
    'password': 'p@ssw0rd1',
    'host': 'mysqldb',
    'database': 'recruiter_db'
}

mydb = mysql.connector.connect(**config)
cursor = mydb.cursor()

