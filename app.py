from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')