#Ao abrir o Gitpod, sempre execute:
# pip install -r requirements.txt
from flask import Flask, render_template, request
import csv
from uuid import uuid4

app = Flask(__name__)

tasks = [
    {'name': 'Insira os jogos da sua biblioteca: '}
]

@app.route('/')
def home():
   with open('jogos.csv', 'rt') as file_in:
    jogos = csv.DictReader(file_in) 
    #templates
    return render_template('home.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    task = {'name': name}
    tasks.append(task)
    return render_template('home.html', tasks=tasks)
    entrada = []
    entrada.append([uuid4(), name])

with open('jogos.csv', 'a') as file_out:
    escritor = csv.writer(file_out)
    escritor.writerows(rows)(entrada)



app.run(debug=True)