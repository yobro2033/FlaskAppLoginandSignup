from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/login')
def login():
    return render_template('login_form.html')

@app.route('/signup')
def signup():
    return render_template('simple_form.html')

@app.route('/insert', methods=['POST'])
def hello():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("INSERT INTO Users (Name, Email, Password) VALUES (?,?,?)",(name,email,password))
    con.commit()
    return 'Hello ' + name +',<p>Thank you for registering account with us! <p>We have successfully sent you an email to the following address ' + email + '.'

@app.route('/select')
def select():
	con = sqlite3.connect('login.db')
	cur = con.cursor()
	cur.execute("SELECT * FROM Users")
	return str(cur.fetchall())

@app.route('/verify', methods=['POST'])
def verify():
	con = sqlite3.connect('login.db')
	cur = con.cursor()
	cur.execute(	"SELECT * FROM Users WHERE Name=? AND Email=? AND Password=?",
    		       (request.form['name'],request.form['email'],request.form['password']))
	result = cur.fetchall()
	resultFinal = str(result)
	if len(resultFinal) == 0:
		return 'Your information submitted is not registered or incorrect!'
	else:
	    return 'You are logged in, ' + request.form['name'] + '!'



