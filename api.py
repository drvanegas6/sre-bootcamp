from flask import Flask
from flask import jsonify
from flask import request
from methods import Token, Restricted
import hashlib, base64
import mysql.connector

Conection_db = mysql.connector.connect( host='localhost', user= 'secret', passwd='noPow3r', port=8000, db='bootcamp_tht' )
cur = Conection_db.cursor()
cur.execute( "SELECT username, password, salt FROM users" )

app = Flask(__name__)
login = Token()
protected = Restricted()


# Just a health check
@app.route("/")
def url_root():
    return "OK"


# Just a health check
@app.route("/_health")
def url_health():
    return "OK"


# e.g. http://127.0.0.1:8000/login
@app.route("/login", methods=['POST'])
def url_login():

    username = request.form['username']
    password = request.form['password']
    salt = request.form['salt']
    saltpass = username+password+salt
    
    res = {
        hashlib.sha256(saltpass.encode()).hexdigest()
        "data": login.generate_token(salt, username, password)
    }
    return jsonify(res)


# # e.g. http://127.0.0.1:8000/protected
@app.route("/protected")
def url_protected():
    auth_token = request.headers.get('Authorization')
    res = {
        "data": protected.access_data(auth_token)
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
    
Conection_db.close()
