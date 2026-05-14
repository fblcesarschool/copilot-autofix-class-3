import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    """
    Vulnerable endpoint - SQL Injection vulnerability
    """
    username = request.form.get('username')
    password = request.form.get('password')
    
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute(query)
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return {'status': 'success', 'message': 'Login successful'}, 200
    else:
        return {'status': 'error', 'message': 'Invalid credentials'}, 401

if __name__ == '__main__':
    app.run(debug=True)
