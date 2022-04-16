import mysql.connector
from datetime import datetime
from email import message
from flask import Flask, render_template, request, url_for, redirect
from database import cursor, mydb
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_db(data):
    
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
    
    sql = "INSERT INTO contact_info (name, email, company, subject, message) VALUES (%s, %s, %s, %s, %s)"
    val = (data['name'], data['email'], data['company'], data['subject'], data['message'])
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")
    #mydb = mysql.connector.connect(
    #    host="mysqldb",
    #    user="root",
    #    passwd="p@ssw0rd1",
    #    database="recruiter_db"
    #)
    
    #mycursor = mydb.cursor()
    #mycursor.execute("CREATE TABLE contact_info (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(50) NOT NULL, email VARCHAR(150) NOT NULL, company VARCHAR(50) NOT NULL, subject VARCHAR(255) NOT NULL, message NOT NULL, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)")
    #sql = "INSERT INTO contact_info (name, email, company, subject, message) VALUES (%s, %s, %s, %s, %s)"
    #val = (data["name"], data["email"], data["company"], data["subject"], data["message"], datetime.now())
    #mycursor.execute(sql, val)
    #mydb.commit()
    #mycursor.close()
    #mydb.close()

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_db(data)
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'somthing went wrong. Try again!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')