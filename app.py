from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #templates
    return render_template('home.html')

@app.route('/bye')
def bye():
    return 'Bye'

app.run(debug=True)