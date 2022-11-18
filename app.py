from flask import Flask, render_template, request

app = Flask(__name__)

tasks = [
    {'name': 'Estudar', 'finished': False},
    {'name': 'Dormir', 'finished': True},
    {'name': 'Comer', 'finished': True}
]

@app.route('/')
def home():
    #templates
    return render_template('home.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    return name

app.run(debug=True)