from flask import Flask, render_template, request

app = Flask(__name__)

tasks = [
    {'name': 'Insira os jogos da sua biblioteca: '}
]

@app.route('/')
def home():
    #templates
    return render_template('home.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    task = {'name': name}
    tasks.append(task)
    return render_template('home.html', tasks=tasks)
    
app.run(debug=True)