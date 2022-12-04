#Ao abrir o Gitpod, sempre execute:
# pip install -r requirements.txt

#todas bibliotecas instaladas
from flask import Flask, render_template, request
import csv
from uuid import uuid4
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
   with open('jogos.csv', 'rt') as file_in:
    jogos = csv.DictReader(file_in) 
    #templates
    return render_template('home.html', jogos=jogos)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    #pega as variaveis do forms
    nome = request.form['nome']
   
    entrada= []
    entrada.append([uuid4(), nome])

    #da append a uma nova row no arquivo .csv
    with open('jogos.csv', 'a') as file_out:
        escritor = csv.writer(file_out)
        escritor.writerows(entrada)

    #redireciona para o "/" do site
    with open('jogos.csv', 'rt') as file_in:
        jogos = csv.DictReader(file_in) 
        return render_template('home.html', jogos=jogos)

#deleta rows de acordo com o id
@app.route('/delete/<id>')
def delete(id):

    data = pd.read_csv("jogos.csv")
    data = data.set_index("Id") 

    data.drop(id, axis='index', inplace=True)

    data.to_csv('jogos.csv')

    with open('jogos.csv', 'rt') as file_in:
        jogos = csv.DictReader(file_in)
        return render_template('home.html', jogos=jogos)

@app.route('/update/<id>/<nome>')
def update(id, nome):
    lista = [id, nome]
    return render_template('update.html', lista=lista)

@app.route('/saveup', methods=['POST'])
def saveup():

    id = request.form['id']
    nome = request.form['nome']

    data = pd.read_csv("jogos.csv")
    
    new_df = pd.DataFrame({'Id': [id], 'Nome': [nome]})

    data = data.set_index("Id")
    new_df = new_df.set_index("Id") 

    data.update(new_df)

    data.to_csv('jogos.csv')

    with open('jogos.csv', 'rt') as file_in:
        jogos = csv.DictReader(file_in)
        return render_template('home.html', jogos=jogos)

app.run(debug=True)