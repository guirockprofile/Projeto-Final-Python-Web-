#Ao abrir o Gitpod, sempre execute:
# pip install -r requirements.txt

#todas bibliotecas instaladas
from flask import Flask, render_template, request
import csv
from uuid import uuid4
import pandas as pd

app = Flask(__name__)

#função que faz a leitura do arquivo .csv e joga os dados para o home.html
@app.route('/')
def home():
   with open('jogos.csv', 'rt') as file_in:
    jogos = csv.DictReader(file_in) 
    #templates
    return render_template('home.html', jogos=jogos)

#função que leva o usuário a página de criação
@app.route('/create')
def create():
    return render_template('create.html')

#função
@app.route('/save', methods=['POST'])
def save():
   
    #pega as variaveis do forms
    nome = request.form['nome']
    plataforma = request.form['plataforma']
   
    entrada= []
    entrada.append([uuid4(), nome, plataforma])

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

    #abre o arquivo .csv pelo pandas
    data = pd.read_csv("jogos.csv")
    #atribui o valor de index para a coluna 'Id'
    data = data.set_index("Id") 
     
    #joga toda variavel com o valor index para a coluna 'Id'
    data.drop(id, axis='index', inplace=True)
    
    #salva o novo dataset
    data.to_csv('jogos.csv')

    #função que faz a leitura do .csv e as joga para o home.html
    with open('jogos.csv', 'rt') as file_in:
        jogos = csv.DictReader(file_in)
        return render_template('home.html', jogos=jogos)

#pega as variaveis row que o usário quer editar, e as insere no forms
@app.route('/update/<id>/<nome>/<plataforma>')
def update(id, nome, plataforma):
    lista = [id, nome, plataforma]
    return render_template('update.html', lista=lista)

#salva os forms que foram modificados pelo usuário
@app.route('/saveup', methods=['POST'])
def saveup():

    #obtem as novas variaveis
    id = request.form['id']
    nome = request.form['nome']
    plataforma = request.form['plataforma']

    #abre o dataframe do .csv
    data = pd.read_csv("jogos.csv")
    
    #cria um novo dataframe apartir das novas variaveis
    new_df = pd.DataFrame({'Id': [id], 'nome': [nome], 'plataforma': [plataforma]})
    
    #atribui os valores de index a coluna 'Id'
    data = data.set_index("Id")
    new_df = new_df.set_index("Id") 

    #atualiza os dados do dataframe
    data.update(new_df)

    #salva o arquivo .csv
    data.to_csv('jogos.csv')

    #redireciona para "/"
    with open('jogos.csv', 'rt') as file_in:
        jogos = csv.DictReader(file_in)
        return render_template('home.html', jogos=jogos)



app.run(debug=True)