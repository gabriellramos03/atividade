"""
@author: Mariela
"""
from flask import Flask 

app_gabriel = Flask (__name__) 

@app_gabriel.route('/')
@app_gabriel.route('/ola')

def raiz():
    return 'Olá, turma!'

def saudacoes (nome):
    return f'Olá, {nome}!'

if __name__ == "__main__" :
    app_gabriel.run(port = 8000)
