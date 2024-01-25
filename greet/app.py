from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def FirstGreeting():
    return "Welcome"

@app.route('/welcome/home')
def SecondGreeting():
    return "Welcome Home"

@app.route('/welcome/back')
def ThirdGreeting():
    return "Welcome Back"