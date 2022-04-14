import mysql.connector
from datetime import datetime
from email import message
from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')
        
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

def write_to_db(data):
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        passwd="p@ssw0rd1",
        database="recruiter_db"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE contact_info (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(50) NOT NULL, email VARCHAR(150) NOT NULL, company VARCHAR(50) NOT NULL, subject VARCHAR(255) NOT NULL, message NOT NULL, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)")
    sql = "INSERT INTO contact_info (name, email, company, subject, message) VALUES (%s, %s, %s, %s, %s)"
    val = (data["name"], data["email"], data["company"], data["subject"], data["message"], datetime.now())
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        #write_to_csv(data)
        write_to_db(data)
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'somthing went wrong. Try again!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')