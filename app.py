import os
from flask import Flask, render_template, request, redirect
import mysql.connector as mysql


app = Flask(__name__)


def establish_connection():
    """
    gain connection
    """
    cnx = mysql.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE'),
        auth_plugin='mysql_native_password'
    )
    return cnx
# to develop localy unhide below function and hide above config 
# def establish_connection():
#     """
#     gain connection
#     """
#     cnx = mysql.connect(
#         user='root', password='',
#         host='localhost',
#         database='testdb',
#         use_pure=False
#     )
#     return cnx

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        fname = userDetails['fname']
        lname = userDetails['lname']
        email = userDetails['email']
        city = userDetails['city']
        state = userDetails['state']
        con=establish_connection()
        cur = con.cursor()
        cur.execute("SHOW TABLES")
        if cur.fetchone():
            cur.execute("INSERT INTO users(fname,lname,email,city,state) VALUES(%s,%s,%s,%s,%s)",(fname,lname,email,city,state))
        else:
            cur.execute("CREATE TABLE users (fname varchar(20),lname varchar(20),email varchar(40),city varchar(20),state varchar(20));")
            cur.execute("INSERT INTO users(fname,lname,email,city,state) VALUES(%s,%s,%s,%s,%s)",(fname,lname,email,city,state))
        con.commit()
        con.close()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    con=establish_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    userDetails=cur.fetchall()
    if len(userDetails) > 0:
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

