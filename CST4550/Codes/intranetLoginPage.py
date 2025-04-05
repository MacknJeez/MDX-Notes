from flask import Flask, request, render_template
from datetime import datetime
import logging
from flask import redirect, url_for

app = Flask(__name__)

#log file
login_logger = logging.getLogger('login_attempts')
login_logger.setLevel(logging.INFO)
handler = logging.FileHandler('login_attempts.log')
handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
login_logger.addHandler(handler)


# Function to validate user credentials
def validate_user(username, password):
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                user, pw = line.strip().split(':')
                if user == username and pw == password:
                    return True
    except FileNotFoundError:
        pass
    return False


# Function to log all login attempts (both failed and successful)
def log_login_attempt(username, success):
    #ip = request.remote_addr 

    #small change, it now takes the IP of the device accessing the link before ngrok proxies it so the logs are accurate
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    
    user_agent = request.headers.get('User-Agent')
    status = 'SUCCESS' if success else 'FAILED'
    login_logger.info(f"LOGIN ATTEMPT | IP: {ip} | Username: {username} | User-Agent: {user_agent} | Status: {status}")

# Welcome route
@app.route('/welcome', methods=['GET'])
def welcome():
    return render_template('welcome.html')  # 'welcome.html' will use the .success-page class


# Home route
@app.route('/')
def home():
    return render_template('home.html')  # A simple homepage with a button to login


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if validate_user(username, password):
            log_login_attempt(username, success=True)  # Log successful login
            return redirect(url_for('welcome'))  # Redirect to the welcome page
        else:
            log_login_attempt(username, success=False)  # Log failed login
            message = 'Invalid credentials.'
    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

