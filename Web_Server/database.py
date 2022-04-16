import mysql.connector

config = {
    'user': 'root',
    'password': 'p@ssw0rd1',
    'host': 'mysqldb',
    'database': 'recruiter_db'
}

mydb = mysql.connector.connect(**config)
cursor = mydb.cursor()

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