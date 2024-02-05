from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Vignesh.9487ks'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the username is a valid email ending with "@bitsathy.ac.in"
    if not username.endswith("@bitsathy.ac.in"):
        return "Invalid email domain"

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()
    cur.close()

    if user:
        # Successful login
        return "Welcome, {}".format(username)
    else:
        # Invalid login
        return "Invalid login"

if __name__ == '__main__':
    app.run(debug=True)
