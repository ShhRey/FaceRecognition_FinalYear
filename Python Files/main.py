from flask import Flask, render_template, url_for, request, redirect, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import createData
import traindataset,cut_face,traintest,list1

app = Flask(__name__)

app.secret_key = 'random'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pythonlogin'
#Initialize MySQL
mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def login():
        if 'username' in session and session['admin'] == 'YES':
                return render_template('admin.html')
        elif 'username' in session and session['admin'] == 'NO':
                return render_template('notadmin.html')
        else:
                if (request.method == 'POST') and ('username' in request.form) and ('password' in request.form):
                        username = request.form['username']
                        password = request.form['password']
                        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                        cursor.execute('SELECT * FROM accounts WHERE username=%s AND password=%s',(username,password))
                        account = cursor.fetchone()
                        if account:
                                session['loggedin'] = True
                                session['id'] = account['id']
                                session['username'] = account['username']
                                session['admin'] = account['admin']
                                if session['admin'] == 'YES':
                                        return render_template('admin.html')
                                elif session['admin'] == 'NO':
                                        return render_template('notadmin.html')
                else:
                        #msg = 'Incorrect Username or Password !'
                        return render_template('index.html')


@app.route('/logout')
def logout():
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop("username", None)
        session.pop("admin", None)
        return redirect(url_for('login'))


@app.route('/register', methods=['GET','POST'])
def register():
        msg = ''
        if (request.method == 'POST') and ('username' in request.form) and ('email' in request.form) and ('password' in request.form):
                username = request.form['username']
                email = request.form['email']
                password = request.form['password']
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM accounts WHERE username=%s AND email=%s AND password=%s',(username,email,password))
                account = cursor.fetchone()
                if account:
                        msg = 'Account already exists!'
                elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                        msg = 'Invalid E-mail Address!'
                elif not re.match(r'[A-Za-z0-9]+', username):
                        msg = 'Username must contain only Characters and Numbers!'
                elif not 'username' or not 'email' or not 'password':
                        msg = 'Please Fill the details!'
                else:
                        cursor.execute('INSERT INTO accounts (username,email,password) VALUES(%s,%s,%s)', (username,email,password))
                        mysql.connection.commit()
                        msg = 'Successfully Registered!'
        return render_template('register.html', msg=msg)

@app.route('/home', methods=['GET','POST'])
def home():
        if 'loggedin' in session:
                render_template('home.html', username=session['username'])
        return redirect(url_for('login'))

@app.route('/addret', methods=['GET','POST'])
def addret():
    
    if request.method == 'POST':
        name = request.form['name']
        regno = request.form['regno']
        year = request.form['year']
        division = request.form['division']
        rollno = request.form['rollno']
        contactno = request.form['contactno']
        createData.createdata(name,regno,year,rollno,contactno,division)
        print("Data created")

    return redirect(url_for('login'))

@app.route('/train', methods=['GET','POST'])
def train():
        traindataset.train()
        return redirect(url_for('login'))

@app.route('/mark', methods=['GET','POST'])
def mark():
        if request.method == 'POST':
                year = request.form['year']
                division = request.form['division']
                divv=year+division
                time = request.form['time']
                day = request.form['day']
        #cut_face.crop()
        #traintest.test()
        print("flask val=",time,divv,day)
        list1.rec(time,divv,day)
        print("recognized")

        return redirect(url_for('login'))

@app.route('/ret', methods=['GET','POST'])
def ret():
        if request.method == 'POST':
                year = request.form['year']
                division = request.form['division']
                regno = request.form['regno']
                
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
