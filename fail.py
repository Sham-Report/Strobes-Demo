from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password))
    result = c.fetchone()

    if result:
        return "Login successful!"
    else:
        return "Invalid username or password."

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
app.run(debug=True)
