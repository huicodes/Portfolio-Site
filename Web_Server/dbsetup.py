import mysql.connector
from mysql.connector import errorcode
from database import cursor

DB_NAME = 'recruiter_db'

TABLES = {}

TABLES['contact_info'] = (
    "CREATE TABLE IF NOT EXISTS `contact_info` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(50) NOT NULL,"
    "  `email` varchar(150) NOT NULL,"
    "  `company` varchar(50) NOT NULL,"
    "  `subject` varchar(255) NOT NULL,"
    "  `message` text NOT NULL,"
    "  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

def create_db():
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
    print(f"Database {DB_NAME} created")
    
def create_tables():
    cursor.execute("USE recruiter_db")
    
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print(f"Creating table ({table_name}) ", end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(f"already exists.")
            else:
                print(err.msg)
        else:
            print(f"OK")    
    
create_db()
create_tables()